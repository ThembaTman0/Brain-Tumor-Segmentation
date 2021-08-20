def resize_images(path):
    no_files = glob.glob('data/'+path+'/no/*.jpg')
    yes_files = glob.glob('data/'+path+'/yes/*.jpg')
    
    # saving no files 0
    for i in range(len(no_files)):
        image=plt.imread(no_files[i])
        image=color.rgb2grey(image)
        image_resized = resize(image,(64,64),
                               anti_aliasing=True)
        
        plt.imsave("new-data/"+path+"/no/"+str(i)+".jpg",image_resized,cmap="gray")
    
    # saving yes files
    for i in range(len(yes_files)):
        image=plt.imread(yes_files[i])
        image=color.rgb2grey(image)
        image_resized = resize(image,(64,64),
                               anti_aliasing=True)
        
        plt.imsave("new-data/"+path+"/yes/"+str(i)+".jpg",image_resized,cmap="gray")
        
