---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-16
title: 如何将图片压缩到指定大小以下
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将图片压缩到指定大小以下
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:66719b2b41d84e455d1cd9a00911a443dd508fb9ddeb79ca6f557326c6abfc10
---

**问题详情：**

目前仅支持通过质量压缩来减小图片大小，尚未提供其他压缩方法将图片压缩到指定大小，例如将PixelMap压缩至30 KB。

**解决措施：**

目前没有直接的接口支持将PixelMap压缩到指定大小以下，但可以通过循环压缩的方式实现。具体方案如下：

1. 调用自定义的compressedImage方法，传入要压缩的图片pixelMap和指定的压缩目标大小。
2. 首先，判断当图片质量参数quality设置为0时，packToData压缩后的图片最小字节大小是否满足指定的图片压缩大小。如果满足，则使用packToData方式通过二分查找，找到最接近指定图片压缩目标大小的quality值，循环压缩图片。如果不满足，则使用scale对图片进行缩放，采用while循环每次递减0.4倍缩放图片，再用packToData（将图片质量参数quality设置为0）获取压缩后的图片大小，最终查找到最接近指定图片压缩目标大小的缩放倍数的图片压缩数据。

   需要注意的是：通过quality压缩图片，不会改变图片的尺寸，且quality太低会导致图片出现伪影，建议quality不低于80。通过scale缩放则会直接改变图片尺寸，图片分辨率建议保持在1080\*1080以上，且建议宽高等比压缩，以避免图片变形。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { common } from '@kit.AbilityKit';

   5. class CompressedImageInfo {
   6. imageUri: string = ""; // URI of compressed image storage location
   7. imageByteLength: number = 0; // Compressed image byte length
   8. }

   10. /**
   11. * Image compression, saving
   12. * @param sourcePixelMap：PixelMap object of the original image to be compressed
   13. * @param maxCompressedImageSize：Specify the compression target size for the image, in kb
   14. * @returns compressedImageInfo：Return the final compressed image information
   15. */
   16. async function compressedImage(sourcePixelMap: image.PixelMap,
   17. maxCompressedImageSize: number): Promise<CompressedImageInfo> {
   18. // Create an ImagePacker object for image encoding
   19. const imagePackerApi = image.createImagePacker();
   20. const IMAGE_QUALITY = 80;
   21. const packOpts: image.PackingOption = { format: "image/jpeg", quality: IMAGE_QUALITY };
   22. // Encode through PixelMap. Compressed ImageData is the image file stream obtained by packaging.
   23. let compressedImageData: ArrayBuffer = await imagePackerApi.packToData(sourcePixelMap, packOpts);

   25. const maxCompressedImageByte = maxCompressedImageSize * 1024;
   26. // Image compression. First, determine whether the minimum byte size of the image that can be compressed by packToData meets the specified image compression size when setting the image quality parameter quality to 80.
   27. // If satisfied, use the packToData method to binary search for the quality closest to the specified image compression target size to compress the image.
   28. // If it is not satisfied, use scale to scale the image first, use a while loop to scale the image by 0.4 times each time,
   29. // then use packToData (with the image quality parameter quality set to 80) to obtain the compressed image size,
   30. // and finally find the compressed image data with the closest scaling factor to the specified image compression target size.
   31. if (maxCompressedImageByte > compressedImageData.byteLength) {
   32. // Using packToData binary compression to obtain image file streams
   33. compressedImageData =
   34. await packingImage(compressedImageData, sourcePixelMap, IMAGE_QUALITY, maxCompressedImageByte);
   35. } else {
   36. // Use scale to scale the image first, use a while loop to decrease the scale by 0.4 times each time, then use packToData (with the image quality parameter quality set to 80) to obtain the compressed image size,
   37. // and finally find the compressed image data with the closest scaling factor to the specified image compression target size
   38. let imageScale = 1;
   39. const REDUCE_SCALE = 0.4;
   40. // Determine whether the compressed image size is greater than the specified compression target size. If it is, continue to reduce the scaling factor for compression.
   41. while (compressedImageData.byteLength > maxCompressedImageByte) {
   42. if (imageScale > 0) {
   43. // Performance knowledge point: As scale directly modifies the PixelMap data of the image, binary search for scale scaling factor is not applicable. Here, we use a cyclic decrease of 0.4 times to scale the image,
   44. // in order to find and determine the most suitable scaling factor. If you do not have high requirements for image compression quality,
   45. // it is recommended to increase the scaling factor reduceScale each time to reduce loops and improve scale compression performance.
   46. imageScale = imageScale - REDUCE_SCALE;
   47. await sourcePixelMap.scale(imageScale, imageScale);
   48. compressedImageData = await packToData(sourcePixelMap, IMAGE_QUALITY);
   49. } else {
   50. // When the imageScale scaling is less than or equal to 0, it is meaningless and the compression ends. We do not consider the case where the image scaling factor is less than reduceScale here.
   51. break;
   52. }
   53. }
   54. }
   55. // Save the image and return the compressed image information.
   56. const compressedImageInfo: CompressedImageInfo = await saveImage(compressedImageData);
   57. return compressedImageInfo;
   58. }

   60. /**
   61. * Packing compression
   62. * @param sourcePixelMap：PixelMap of the original image to be compressed
   63. * @param imageQuality：Image quality parameters
   64. * @returns data：Return compressed image data
   65. */
   66. async function packToData(sourcePixelMap: image.PixelMap, imageQuality: number): Promise<ArrayBuffer> {
   67. const imagePackerApi = image.createImagePacker();
   68. const packOpts: image.PackingOption = { format: "image/jpeg", quality: imageQuality };
   69. const data: ArrayBuffer = await imagePackerApi.packToData(sourcePixelMap, packOpts);
   70. return data;
   71. }

   73. /**
   74. * Packing binary method cyclic compression
   75. * @param compressedImageData：Arrays Buffer for image compression
   76. * @param sourcePixelMap：PixelMap of the original image to be compressed
   77. * @param imageQuality：Image quality parameters
   78. * @param maxCompressedImageByte：Compress the byte length of the target image
   79. * @returns compressedImageData：Return the compressed image data after binary packToData
   80. */
   81. async function packingImage(compressedImageData: ArrayBuffer, sourcePixelMap: image.PixelMap, imageQuality: number,
   82. maxCompressedImageByte: number): Promise<ArrayBuffer> {
   83. // The range of image quality parameters is 80-100. Here, an array for packToData binary image quality parameters is created with 5 as the minimum binary unit.
   84. const packingArray: number[] = [];
   85. const DICHOTOMY_ACCURACY = 5;
   86. // Performance knowledge point: If the requirements for image compression quality are not high, it is recommended to increase the minimum binary unit dichotomyAccuracy,
   87. // reduce loops, and improve packToData compression performance.
   88. for (let i = 80; i <= 100; i += DICHOTOMY_ACCURACY) {
   89. packingArray.push(i);
   90. }
   91. let left = 0;
   92. let right = packingArray.length - 1;
   93. // Binary compressed image
   94. while (left <= right) {
   95. const mid = Math.floor((left + right) / 2);
   96. imageQuality = packingArray[mid];
   97. compressedImageData = await packToData(sourcePixelMap, imageQuality);
   98. // Perform packToData compression based on the input image quality parameters and return the compressed image file stream data.
   99. if (compressedImageData.byteLength <= maxCompressedImageByte) {
   100. left = mid + 1;
   101. if (mid === packingArray.length - 1) {
   102. break;
   103. }
   104. // Obtain the compressed image file stream data with the next binary image quality parameter (mid+1)
   105. compressedImageData = await packToData(sourcePixelMap, packingArray[mid + 1]);
   106. // Determine whether the size of the image compressed with the next image quality parameter (mid+1) is greater than the specified compression target size of the image.
   107. // If it is greater than, it indicates that the current image quality parameter (mid) compresses the image size closest to the compression target size of the specified image.
   108. // Pass in the current image quality parameter mid to obtain the final compressed data of the target image.
   109. if (compressedImageData.byteLength > maxCompressedImageByte) {
   110. compressedImageData = await packToData(sourcePixelMap, packingArray[mid]);
   111. break;
   112. }
   113. } else {
   114. // The target value is not in the right half of the current range. Move the right boundary of the search range to the left to narrow down the search range
   115. // and continue searching for the left half in the next iteration.
   116. right = mid - 1;
   117. }
   118. }
   119. return compressedImageData;
   120. }

   122. /**
   123. * pictures saving
   124. * @param compressedImageData：Compressed image data
   125. * @returns compressedImageInfo：Return compressed image information
   126. */
   127. async function saveImage(compressedImageData: ArrayBuffer): Promise<CompressedImageInfo> {
   128. // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext
   129. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   130. // Define the compressed image URI to be saved. AfterCompression.jpeg represents the compressed image.
   131. const compressedImageUri: string = context.filesDir + '/' + 'afterCompression.jpeg';
   132. try {
   133. const res = fileIo.accessSync(compressedImageUri);
   134. if (res) {
   135. // If the image afterCompression.jpeg already exists, delete it
   136. fileIo.unlinkSync(compressedImageUri);
   137. }
   138. } catch (err) {
   139. console.error(`AccessSync failed with error message: ${err.message}, error code: ${err.code}`);
   140. }
   141. // Knowledge point: Save images. Obtain the final compressed image data compressed ImageData and save the image.
   142. // Compress image data and write it to a file
   143. const file: fileIo.File = fileIo.openSync(compressedImageUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   144. fileIo.writeSync(file.fd, compressedImageData);
   145. fileIo.closeSync(file);
   146. // Obtain compressed image information
   147. let compressedImageInfo: CompressedImageInfo = new CompressedImageInfo();
   148. compressedImageInfo.imageUri = compressedImageUri;
   149. compressedImageInfo.imageByteLength = compressedImageData.byteLength;
   150. return compressedImageInfo;
   151. }
   ```

   [CompressedImage.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/CompressedImage.ets#L21-L172)
