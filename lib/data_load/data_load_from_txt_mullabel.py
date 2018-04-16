# _*_ coding: utf-8 _*_
"""
@author: lixihua9@126.com
@date:   20180417
@brief:  data_load_from_txt_mullabel
"""

from lib.utils.multi_label_utils import shuffle_train_data


class data_load_from_txt_mullabel(object):

    def __init__(self, img_dir, train_rate):
        self.img_dir = img_dir
        self.train_imgs = []
        self.train_labels = []
        self.train_rate = train_rate
        self.note_label = []
    
    def _gen_img_path(self):
        data_lines = open(self.img_dir, 'r').readlines() 
        for line in data_lines:
            img_path = line.split(' ')[0]
            img_label = line.split(' ')[1].split('\n')[0].split(',')
            k = []
            for label in img_label:
              k += [int(label)]
            self.train_imgs.append(img_path)
            self.train_labels.append(k)
        self.train_imgs, self.train_labels = shuffle_train_data(self.train_imgs, self.train_labels)
    
    def gen_train_valid(self):
        self._gen_img_path()
        image_n = len(self.train_imgs)
        train_n = int(image_n*self.train_rate)
        valid_n = int(image_n*(1 - self.train_rate))
        train_data, train_label = self.train_imgs[0:train_n], self.train_labels[0:train_n]
        valid_data, valid_label = self.train_imgs[train_n:image_n], self.train_labels[train_n:image_n]
        
        return train_data, train_label, valid_data, valid_label, train_n, valid_n, self.note_label

# 以下测试用
if __name__ == '__main__':
    data = data_load_from_txt_mullabel('train.txt', 0.9)
    train_data, train_label, valid_data, valid_label, train_n, valid_n, _ = data.gen_train_valid()
    print(train_data)
    print(train_label)
