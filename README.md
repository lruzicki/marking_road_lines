# marking_road_lines

Python program using cv2, numpy, matplotlib to draw red line on the marking of road lines.

Result:
![alt-text](https://github.com/lukruz/marking_road_lines/blob/main/result3.gif?raw=true)

About:

First I used video capture provided by cv2 to loop the video frame by frame.
![s1](https://user-images.githubusercontent.com/56487722/172052567-c94f27b4-b5f3-4465-b9fb-e9084db05bcf.jpg)

Frame must be converted into gray...
![s2](https://user-images.githubusercontent.com/56487722/172052623-5d1648c9-bc3a-4c4a-bae7-8e8b0d9ed196.jpg)

...then blurred.
![s3](https://user-images.githubusercontent.com/56487722/172052620-47a94a62-0b19-4873-b42c-b3e55c7e6c16.jpg)

Then it is possible for the program to use canny to detect edges. User must fit the lower and higher treshold to get low number of edges.
![s4](https://user-images.githubusercontent.com/56487722/172052614-08611b0d-3f2a-4c70-a544-7423beb4e060.jpg)

User also has to crop the frame to include only part where is the road. The more accurate it is the better program is going to work.
![s5](https://user-images.githubusercontent.com/56487722/172052613-6dce294f-5605-403b-8809-f8345611fc72.jpg)

Next we can use hough lines to draw red lines in final destination of frame.
![s6](https://user-images.githubusercontent.com/56487722/172052609-d33b10f4-3cff-439b-85d7-afc365e667fe.jpg)

Last but not least program sum the raw frame with generated lines.
![s7](https://user-images.githubusercontent.com/56487722/172052606-a591049d-6447-453d-92ad-41fd1efeaae4.jpg)

It also counts number of frames and display my name on the video.
