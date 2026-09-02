---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-glossary
title: Cloud Foundation Kit术语
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:fe8f4517f2799bf1639a2aa0e039bfada3137e8ef311aec032f5ded622b75b7e
---

## C

### Cloud DB；云数据库

Cloud Foundation Kit提供的云端数据库服务，提供数据存储和查询能力，适用于需要实时数据协作的场景。

### Cloud DB Zone；数据库存储区

云数据库中的逻辑存储单元，用于对数据进行分区管理。

### Cloud Functions；云函数

Cloud Foundation Kit提供的云端函数Serverless计算服务，开发者只需聚焦业务逻辑，使用函数开发核心业务代码并上传到云端，云端接管函数的运行并保证资源的高可用与伸缩。

### Cloud Storage；云存储

Cloud Foundation Kit提供的云端文件存储服务，支持上传、下载、管理文件，适用于存储用户生成的内容或静态资源。

## D

### Debug Credential；调试凭据

模拟器调试时使用的临时访问凭证，需在AppGallery Connect云侧注册后用于验证HarmonyOS应用/元服务对Cloud Foundation Kit的访问。

## I

### Install Prefetch；安装预加载

预加载类型之一，适用于应用安装后首次打开场景，在应用安装时下载云侧数据到本地缓存。数据仅允许调用一次。

## L

### Link Prefetch；跳链安装预加载

预加载类型之一，结合App Linking Kit的延迟链接功能，在应用安装过程中预加载详情页数据，用户首次打开即可跳转。应用安装后10分钟内有效。

### Local Cloud Function；本地云函数

使用DevEco Studio在端云一体化云侧工程下创建函数、开发函数、调试函数，生成本地函数的Function URI，在端侧工程中触发调用。

## M

### Metadata；元数据

云存储文件中包含的文件属性信息，包括文件名、文件大小、文件类型、创建时间等，也包括用户自定义属性。

## P

### Paginated Query；分页查询

使用云数据库limit限定查询数据，返回数据的起始位置和数量，实现数据分页展示。

### Periodic Prefetch；周期性预加载

预加载类型之一，系统每隔12小时拉取指定页面数据并缓存到本地，适用于节日主题资源、H5离线包等需要定期更新内容的场景。

### Prefetch；预加载

Cloud Foundation Kit提供的数据预加载服务，可将页面所需的文本、图片、音频、视频等资源提前加载到本地缓存，以提升应用页面加载速度。

## S

### Storage Instance；存储实例

云存储的存储实例，用于管理云端文件的上传、下载、获取文件列表、设置或获取元数据等操作。
