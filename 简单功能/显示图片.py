import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
 
pic = mpimg.imread(r'/pic/demo1.jpg') 
plt.imshow(pic) # 显示图片
# plt.axis('off') # 不显示坐标轴
