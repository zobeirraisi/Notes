# Convert qud boxes into rotated box
# In this file we convert quadrilateral .txt files into rotated bounding boxes
import os
import numpy as np
import cv2

INPUT = 'gt'
OUTPUT ='rotated_gt'


def quad_2_rbox(quads):
    # http://fromwiz.com/share/s/34GeEW1RFx7x2iIM0z1ZXVvc2yLl5t2fTkEg2ZVhJR2n50xg
    if len(quads.shape) == 1:
        quads = quads[np.newaxis, :]
    rboxs = np.zeros((quads.shape[0], 5), dtype=np.float32)
    for i, quad in enumerate(quads):
        rbox = cv2.minAreaRect(quad.reshape([4, 2]))
        x, y, w, h, t = rbox[0][0], rbox[0][1], rbox[1][0], rbox[1][1], rbox[2]
        # print(f'x={x},y={y},w={w},h={h},t={t}')
        if np.abs(t) < 45.0:
            rboxs[i, :] = np.array([x, y, w, h, (t * 3.1416/180)])
        elif np.abs(t) > 45.0:
            rboxs[i, :] = np.array([x, y, h, w, (90.0 + t)*3.1416/180])
        else:
            if w > h:
                rboxs[i, :] = np.array([x, y, w, h, (-45.0)*3.1416/180])
            else:
                rboxs[i, :] = np.array([x, y, h, w, (45*3.1416/180)])
    # (x_ctr, y_ctr, w, h) -> (x1, y1, x2, y2)
    # print(rboxs)
    # print('------------------')
    rboxs[:, 0:2] = rboxs[:, 0:2] - rboxs[:, 2:4] * 0.5
    # rboxs[:, 2:4] = rboxs[:, 0:2] + rboxs[:, 2:4]
    rboxs[:, 0:4] = rboxs[:, 0:4].astype(np.int32)
    return rboxs


for Txtfiles in os.listdir(INPUT):
    # print(Txtfiles)
    with open(os.path.join(OUTPUT,Txtfiles),'w') as g:
        with open(os.path.join(INPUT,Txtfiles), encoding='utf-8-sig') as f:
            lines=f.readlines()
            # print(lines)
            for line in lines:
                tag=line.split(',')[-1]
                if tag != "###\n":
                    quads = np.fromstring(line, dtype=int, sep=',')
                    # print(quads)
                    # print(len(quads))
                    if len(quads)>=9:
                        quads=quads[:8]
                    # print(quads)
                    rboxs=quad_2_rbox(quads).flatten()
                    # print(rboxs)
                    rbox2=np.hstack((rboxs,[tag]))
        # break
                    # print(int(float(rbox2[0])))
                    g.write(f'{int(float(rbox2[0]))},{int(float(rbox2[1]))},{int(float(rbox2[2]))},{int(float(rbox2[3]))},{float(rbox2[4]):.4f},{rbox2[5]}')

print('done')
