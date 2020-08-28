from torch.utils.data import Dataset
class Imageset(Dataset):
  

    def __init__(self, 
                data,
                transform=None):
        print('Loading data')
        self.data_list = data      
        print('Done loading data')
 
        self.transform = transform
        self.length = len(self.data_list)
        print('Length', self.length)       

 
    def __getitem__(self,index): 

        if self.transform is not None:
             img = self.transform(self.data_list[index])

        return img

    def __len__(self):
        return self.length