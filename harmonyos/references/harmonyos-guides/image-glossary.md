---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-glossary
title: Image Kit术语
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > Image Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:af058f6a1a019ef5578f22aad05f543285f1df6fde3fad7068702bce0a9b787c
---

## A

### Animated Image；动图

由多帧图像按时间顺序播放形成的图片资源。

### Auxiliary Picture；辅助图

多图对象Picture中与主图配套存储的附加图像数据，通常不独立用于显示，而是作为辅助数据参与HDR合成、深度信息提取或原图恢复等图像处理流程。

## C

### Color Space Conversion；色彩空间转换

在sRGB、Display P3等不同色彩空间之间转换图像颜色表达的处理过程，用于适配不同设备或显示链路的颜色管理需求。

## D

### Depth Map；深度图

记录像素距离或深度信息的辅助图，可用于3D重建、背景分离等依赖场景深度的处理。

### Digital Negative (DNG)；数字负片

Adobe推出的公开RAW图像文件格式，用于保存相机传感器采集的原始图像数据及拍摄相关元数据，可作为不同软件处理RAW图像时的通用格式。

### Direct Memory Access (DMA) Memory；DMA内存

可由解码器、GPU或显示链路直接访问的图像缓冲内存类型，用于减少图片显示链路中的数据拷贝和纹理上传开销。

### Downsampling Decode；下采样解码

通过指定期望输出尺寸，使解码器按合适采样率输出较小图像的解码方式，用于大图预览等需要减少内存占用和解码耗时的场景。

### Dynamic Range；动态范围

图像可表达的亮度信息范围。解码和处理链路可根据动态范围策略输出HDR或SDR结果。

## E

### Exchangeable image file format (Exif)；可交换图像文件格式

记录照片属性和拍摄信息的图像元数据格式，可包含拍摄时间、方向、焦距、地理位置等字段。

### Extensible Metadata Platform (XMP)；可扩展元数据平台

一种用于描述和交换图像元数据的可扩展格式，可记录作者、版权、编辑历史等结构化信息。

## F

### Filter Chain；滤镜链

按顺序组合多个滤镜的图像效果处理链路，用于在一次编辑流程中叠加多种图像处理效果。

### Fragment Map；水印裁剪图

记录原图中被水印遮挡区域的辅助图，可用于水印移除、原图恢复等后处理场景。

## G

### GainMap；增益图

表示亮度增益信息的辅助图。带GainMap的图片可在兼容SDR主图的基础上，为支持HDR的设备生成更高动态范围的显示结果。

## H

### HDR Dual-layer Image；HDR双层图

由主图和GainMap等辅助数据共同表达HDR效果的图像形态，处理时可按需合成为单层HDR图。

### HDR Single-layer Image；HDR单层图

在单一图像层中承载HDR显示信息的图像形态，可由HDR双层图合成得到，也可拆分为主图和GainMap等数据。

### High Dynamic Range (HDR)；高动态范围

高动态范围图像表达方式，可记录更丰富的亮度层次和色彩信息，显示效果受图片数据、设备能力和处理链路影响。

### High Efficiency Image File Format (HEIF)；高效率图像文件格式

一种基于容器结构的高效图像文件格式，可用于封装图像数据及相关信息。相比JPEG，HEIF通常能在保证相近图像质量的同时减小文件体积，但兼容性依赖设备和软件支持。

### HEIF Sequence (HEIFS)；HEIF序列图像

HEIF序列图像格式，通常使用.heifs扩展名，可表示多帧图像及其播放时序信息。

## I

### Image Decoding；图片解码

将所支持格式的图片文件解析并转换为PixelMap或Picture等图像对象的过程，用于后续显示或图像处理。

### Image Encoding；图片编码

将处理后的图像数据封装为指定图片格式文件的过程，用于保存、传输或格式转换。

### Image Metadata；图片元数据

描述图像属性、拍摄信息、格式信息或处理辅助信息的数据集合，可供读取、修改或参与后续图像处理。

## L

### Linear Map；线性图

用于视觉效果增强和色彩后期处理的辅助图。

## P

### Picture；多图对象

Image Kit中的多图对象。由主图、辅助图和元数据组成，支持获取主图、辅助图、元数据以及合成HDR图等操作。

### PixelMap；位图对象

Image Kit中用于承载一张图片像素数据的位图对象，可读取或写入像素数据，并支持裁剪、缩放、旋转、镜像等图像处理操作。

### Pixel Format；像素格式

描述像素数据在内存中如何排列和表达颜色分量的格式，会影响内存占用、透明度能力及解码处理路径。

## R

### RAW Data；RAW数据

直接保留图像传感器原始信息且未经过有损压缩的图像数据，适合需要自定义算法和高质量后处理的场景。

### Region Decode；区域解码

仅解码原图指定矩形区域的方式，适合只需查看或处理图片局部的场景。

## S

### Standard Dynamic Range (SDR)；标准动态范围

标准动态范围图像表达方式，其可表达的亮度范围低于HDR，适用于普通显示设备和常规图像处理场景。

### Stride；步幅

图像在内存中每一行像素数据的存储宽度。其值可能因硬件对齐和内存分配方式大于图片实际宽度，处理像素缓冲区时需要正确使用。

## Y

### YUV Pixel Format；YUV像素格式

以亮度分量和色度分量表达图像的像素格式。文档中的NV12、NV21等格式可在预览和大图显示场景降低内存占用。
