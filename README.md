# marking_road_lines

Python program using cv2, numpy, matplotlib to draw red line on the marking of road lines.

Result:
![alt-text](https://github.com/lukruz/marking_road_lines/blob/main/result3.gif?raw=true))

About:

First I used video capture provided by cv2 to loop the video frame by frame.
Frame must be converted into gray, the blurred. Then it is possible for the program to use canny to detect edges. User must fit the lower and higher treshold to get low number of edges. User also has to crop the frame to include only part where is the road. The more accurate it is the better program is going to work. Next we can use hough lines to draw red lines in final destination of frame. Last but not least program sum the raw frame with generated lines.

It also counts number of frames and display my name on the video.
