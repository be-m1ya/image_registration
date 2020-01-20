import cv2
import numpy as np
from PIL import Image

#テンプレートマッチングで用いる領域切り取り
def crop_img(img, position):
    crop = [0]*3
    for i, posi in enumerate(position):
        crop[i] = img.crop((posi[0,0], posi[0,1], posi[1,0], posi[1,1]))
    return crop
 
#テンプレートマッチング
def match_template(temp,img):
    #only use max_loc
    max_loc = [0]*3

    for i,(temp,img) in enumerate(zip(temp,img)):
        res = cv2.matchTemplate(img,temp,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc[i] = cv2.minMaxLoc(res)             
    return max_loc

#対応する点を示した画像を生成
def make_match_point_img1(img, position, color, save_location):
    for i, posi in enumerate(position):
        cv2.rectangle(img, posi[0], posi[1] ,color,2 )
        cv2.circle(img, (posi[0]), 4 ,(0,0,255))
    cv2.imwrite(save_location + "check_match_point_im2.png", img )

def make_match_point_img2(img, position, match_loc, color, save_location):
    for i, (posi,match) in enumerate(zip(position,match_loc)):
        cv2.rectangle(img, posi[0], posi[1] ,color,2 )
        cv2.circle(img, (posi[0,0]+match[0], posi[0,1]+match[1]), 4 ,(0,0,255))
    cv2.imwrite(save_location + "check_match_point_im1.png", img )    


#アフィン変換と変換後の画像生成
def affine_transform(img1, img2, posi1, posi2, match_loc, save_location):
    rows,cols = img1.size
    pts1 = np.float32([ [posi1[0,0]],[posi1[1,0]],[posi1[2,0]] ])
    pts2 = np.float32([ [posi[0,0]+match[0], posi[0,1]+match[1]],
                        [posi[1,0]+match[0], posi[1,1]+match[1]],
                        [posi[2,0]+match[0], posi[2,1]+match[1]] ])
    
    M = cv2.getAffineTransform(pts1,pts2)
    dst = cv2.warpAffine(np.array(img2),M,(rows,cols))
    cv2.imwrite(save_location + 'template_matching.png',dst)
