### Batch converting PNG to JPG
`for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done`
### copy file with progress 
`rsync -ah --progress source destination`

### number of lines in `<filename>`
`wc -l filename.txt`
### convert images to gif
`convert -delay 20 -loop 0 *.jpg myimage.gif`
### copy multiple files from a list:
`xargs -a list.txt cp -t new_folder`
### watch the siz of folders :
`du -h --max-depth=1`
### Batch resizing converting (check the ! for ignoring the aspect ratio)
`for i in *.jpg ; do convert -resize 256x256! "$i" "${i%.*}.jpg" ; done`
