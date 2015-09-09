
one = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/1.png") 
arrayOne = getPixels(one)
print arrayOne[0]

two = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/2.png") 
arrayTwo = getPixels(two)
print arrayTwo[0]

three = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/3.png") 
arrayThree = getPixels(three)
print arrayThree[0]

four = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/4.png") 
arrayFour = getPixels(four)
print arrayFour[0]

five = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/5.png") 
arrayFive = getPixels(five)
print arrayFive[0]

six = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/6.png") 
arraySix = getPixels(six)
print arraySix[0]

seven = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/7.png") 
arraySeven = getPixels(seven)
print arraySeven[0]

eight = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/8.png") 
arrayEight = getPixels(eight)
print arrayEight[0]

nine = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/9.png") 
arrayNine = getPixels(nine)
print arrayNine[0]

newPic = makePicture("//Users/kjerstifagerholt/Desktop/CST205/cst205-multimedia/images/9.png")
arrayNew = getPixels(newPic)

for i in range(len(arrayNew)):
 arrayRed = [getRed(arrayOne[i]),getRed(arrayTwo[i]),getRed(arrayThree[i]),getRed(arrayFour[i]),getRed(arrayFive[i]),getRed(arraySix[i]),getRed(arraySeven[i]),getRed(arrayEight[i]), getRed(arrayNine[i])]
 arrayGreen = [getGreen(arrayOne[i]),getGreen(arrayTwo[i]),getGreen(arrayThree[i]),getGreen(arrayFour[i]),getGreen(arrayFive[i]),getGreen(arraySix[i]),getGreen(arraySeven[i]),getGreen(arrayEight[i]), getGreen(arrayNine[i])]
 arrayBlue = [getBlue(arrayOne[i]),getBlue(arrayTwo[i]),getBlue(arrayThree[i]),getBlue(arrayFour[i]),getBlue(arrayFive[i]),getBlue(arraySix[i]),getBlue(arraySeven[i]),getBlue(arrayEight[i]), getBlue(arrayNine[i])]
 
 arrayRed.sort() 
 arrayGreen.sort()
 arrayBlue.sort()
 
 #Find the median
 redMedian = arrayRed[4]
 greenMedian = arrayGreen[4]
 blueMedian = arrayBlue[4]
 
 #Set new pixel RGB in new picture

 pixel = arrayNew[i]
 setColor(pixel,(Color(redMedian,greenMedian, blueMedian)))
 arrayNew[i] = pixel
 

 
repaint(newPic) 

 
 
 
 



