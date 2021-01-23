### Batch converting PNG to JPG
`for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done`
### copy file with progress 
`rsync -ah --progress source destination`
