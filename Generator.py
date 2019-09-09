from PIL import Image,ImageOps
import matplotlib.pyplot as plt


white  = (255,255,255)
width  = 3000
lenth  = 4000
img    = Image.open('qitcs.jpg')
#img_qitcs   = img.resize((300,300))

#Prepear title
FinalImg = Image.new('RGB',(width,lenth),white)
FinalImg.paste(img,(0,0))

# read name

file = open("name_list.txt","r")

name = []
affl = []
city = []
#Repeat for each song in the text file

n=0
for line in file:

    plt.figure(num=n,figsize=(2.5, 4))
    t=plt.text(700, lenth*0.08, 'Workshop on New Methods for',
             fontsize=9)
    t=plt.text(750, lenth*0.12, 'Strongly Correlated Electrons',
             fontsize=9)

    #Let's split the line into an array called "fields" using the ";" as a separator:
    fields = line.split(",")
    name.append(fields[0])
    affl.append(fields[1])
    city.append(fields[2])

    t=plt.text(width*0.5,lenth*0.5, name[n],
               verticalalignment='bottom', 
               horizontalalignment='center',
               fontsize=18, fontweight='bold')
    
    t=plt.text(width*0.5,lenth*0.55, affl[n],
               verticalalignment='top',
               horizontalalignment='center',
               fontsize=12)
    
    t=plt.text(width*0.5,lenth*0.6, city[n],
               verticalalignment='top',
               horizontalalignment='center',
               fontsize=12)
    
    t=plt.text(width*0.5,lenth*0.9, "Oct.09-Oct.13 2019, Qingdao",
               verticalalignment='top',
               horizontalalignment='center',
               fontsize=10)
    
    
    plt.axis('off') 
    plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
    plt.imshow(FinalImg)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    name[n].replace(' ','_')
    plt.savefig(name[n]+'.pdf',dpi=300, bbox_inches='tight')
    #plt.show()
    n=n+1


