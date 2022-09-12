import os
from typing import List
import matplotlib.pyplot as plt
import cv2
import numpy as np
from tqdm import tqdm
import pandas as pd


def _crop(img, set_size):

    h, w, c = img.shape

    if set_size > min(h, w):
        return img

    crop_width = int(set_size*1.7)
    crop_height = int(set_size)

    mid_x, mid_y = w//7*3, h//7*4
    offset_x, offset_y = crop_width//2, crop_height//2
       
    crop_img = img[mid_y - offset_y:mid_y + offset_y, mid_x - offset_x:mid_x + offset_x]
    return crop_img


def fourier(filename: str, show: bool=False, crop:bool = False) -> np.ndarray:
    img = cv2.imread(filename)

    if crop:
        img = _crop(img, 650)

        dirs = filename.split("/") 
        new_folder =  f"./croped/{dirs[1]}/{dirs[2]}/"  
        os.makedirs(new_folder, exist_ok=True)
        cv2.imwrite(f"{new_folder}/{dirs[4]}",img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # height, width = gray.shape

    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    # dft_shift = dft
    out = 20*np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    fft_flat = out.flatten()
    # print(f"min:{np.mean(fft_flat)}, max:{np.max(fft_flat)} , mean:{np.mean(fft_flat)} , median:{np.median(fft_flat)} ")

    inverse_shift = np.fft.fftshift(dft_shift)
    inverse_dft = cv2.dft(inverse_shift, flags=cv2.DFT_INVERSE)
    out2 = cv2.magnitude(inverse_dft[:, :, 0], inverse_dft[:, :, 1])

    if show:
        plt.figure(figsize=(10,4))
        plt.subplot(141)
        plt.imshow(gray, cmap='gray')
        plt.title('original')
        plt.subplot(142)
        plt.imshow(out, cmap='gray')
        plt.title('dft')
        plt.subplot(143)
        plt.hist(fft_flat, bins=20)
        plt.title('fft_hist')
        plt.subplot(144)
        plt.imshow(out2, cmap='gray')
        plt.title('inverse')

        plt.show()

    return out

def _get_leaf_folders(root: str) -> List[str]:
    leaf_dir_dict = dict()
    total_files = 0
    for elem in os.walk(root):
        if len(elem[1]) == 0:  # leaf directory
            leaf_dir_dict[elem[0]] = elem[2]
            total_files += len(elem[2])
    # print(leaf_dir_list)
    return leaf_dir_dict, total_files

        
def _make_record(filepath: str, fft: np.array) -> dict:
    folders = filepath.split('/')
    if len(folders) < 4:
        return None
    return dict(
        camera=folders[1],
        display=folders[2],
        moire_degree=folders[3],
        median=np.median(fft),
        mean=np.mean(fft),
        path=filepath,
        std=np.std(fft),
        min=np.min(fft),
        max=np.max(fft),
    )
    


if __name__ == "__main__":
    num = 5
    leaf_dir_dict, total_files = _get_leaf_folders(f'images{num}')
    data_list = list()
    with tqdm(total=total_files) as pbar:
        for leaf_dir, files in leaf_dir_dict.items():
            for file in files:
                filepath = f"{leaf_dir}/{file}"
                fft = fourier(filepath)
                data = _make_record(filepath, fft)
                data_list.append(data)

                pbar.update(1)
                pbar.set_description(
                    f"{filepath}/median:{data['median']:.2f}/mean:{data['mean']:.2f}"
                    )
    df = pd.DataFrame(data_list)
    print(df)
    df.to_csv(f"t_{num}.csv")

    # filename = "images/m_l.jpg"
    # fourier(filename)