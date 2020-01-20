from PIL import Image
import cv2
import numpy as np
import sys
import argparse
import os
import def_list #def_list.pyに使用する関数を定義

if __name__ == "__main__":
    #コマンドライン引数を用いる
    parser = argparse.ArgumentParser(description="input 2 img file (and save location)")
    parser.add_argument("-im1","--image1",required=True, help = "input image1 file")
    parser.add_argument("-im2","--image2",required=True, help = "input image2 file")
    parser.add_argument("-dir1","--match_point_dir", help = "input save_dir for matching point check", default = "check_match_point/")
    parser.add_argument("-dir2","--affine_transform_dir", help = "input save_dir for affine transeform image", default = "affine_trainsform/")
    
    args = parser.parse_args()

     #グレースケールで画像をロード
    img1_pil = Image.open(args.im1).convert('L')
    img2_pil = Image.open(args.im2).convert('L')

    #テンプレートマッチングする3つの領域を選択 [[左下],[右上]]
    img1_posi = np.array([ [[962,661],[999,712]] , [[42,614],[91,660]], [[367,33],[416,74]] ])
    img2_posi = np.array([ [[915,628],[1001,724]] , [[5,601],[117,708]], [[293,27],[389,104]] ])
  
    #各画像における3つの領域を切り取り
    img1_crop = def_list.crop_img(img1_pil,img1_posi)
    img2_crop = def_list.crop_img(img2_pil,img2_posi)

    #PIL -> numpy
    img1_crop = np.array([np.asarray(i) for i in img1_crop])
    img2_crop = np.array([np.asarray(i) for i in img2_crop])

    #テンプレートマッチング
    match_loc = def_list.match_template(img1_crop,img2_crop)

    #テンプレートマッチングの領域と,画像の対応する点を書き出し
    def_list.print_rectangle(img1,img1_posi,(0,0,255),dir1)
    def_list.print_rectangle(img2,img2_posi,match_loc,(255,0,0),dir1)

    #アフィン変換
    affine_transform(img1_pil,img2_pil,img1_posi,img2_posi,match_loc,dir2)
    
