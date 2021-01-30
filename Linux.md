### Batch converting PNG to JPG
`for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done`
### copy file with progress 
`rsync -ah --progress source destination`

### number of lines in `<filename>`
`wc -l filename.txt`
### convert images to gif
`convert -delay 20 -loop 0 *.jpg myimage.gif`
