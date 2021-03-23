import os
import json

INPUT='labels'
OUTPUT='gt'

Files=os.listdir(INPUT)
for file in Files:
    print(file)
    with open(os.path.join(INPUT,file)) as f:
        jf=json.load(f)
        # print(jf)
        imgfile=jf['imgfile']
        img=imgfile.split('/')[-1]
        txt=img.split('.')[0]+'.txt'
        bboxes=jf['bbox']
        text=jf['text']
        # print(imgfile)
        with open(os.path.join(OUTPUT,txt),'w') as g:
            # bboxes=jf['bbox'][0]
            # print(bboxes)
            for i,box in enumerate(bboxes):
                # print(box)
                g.write(f'{str(box[0])},{str(box[1])},{str(box[2])},{str(box[3])},{str(box[4])},{str(box[5])},{str(box[6])},{str(box[7])},xxx\n')

print('done')
