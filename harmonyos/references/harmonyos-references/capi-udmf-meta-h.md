---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-meta-h
title: udmf_meta.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > udmf_meta.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:af8740daa81a4e121d9ba2006db3bc7bb2cd4b18144c5863699e2721ccbea9e8
---

## 概述

PhonePC/2in1TabletTV

声明统一类型数据信息。

**引用文件：** <database/udmf/udmf\_meta.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：** [UDMF](capi-udmf.md)

## 汇总

PhonePC/2in1TabletTV

### 宏定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| UDMF\_META\_ENTITY "general.entity" | 所有表示物理存储类型的基类型，用于描述类型的物理属性，无归属类型。  **起始版本：** 12 |
| UDMF\_META\_OBJECT "general.object" | 所有表示逻辑内容类型的基类型，用于描述类型的功能性特征，无归属类型。  **起始版本：** 12 |
| UDMF\_META\_COMPOSITE\_OBJECT "general.composite-object" | 所有组合内容类型（例如PDF文件类型混合了文本和图片类数据）的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_TEXT "general.text" | 所有文本的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_PLAIN\_TEXT "general.plain-text" | 未指定编码的文本类型，没有标识符，归属类型为TEXT。  **起始版本：** 12 |
| UDMF\_META\_HTML "general.html" | HTML文本类型，归属类型为TEXT。  **起始版本：** 12 |
| UDMF\_META\_HYPERLINK "general.hyperlink" | 超链接类型，归属类型为TEXT。  **起始版本：** 12 |
| UDMF\_META\_XML "general.xml" | XML文本类型，归属类型为TEXT。  **起始版本：** 12 |
| UDMF\_META\_SOURCE\_CODE "general.source-code" | 所有源代码的基类型，归属类型为PLAIN\_TEXT。  **起始版本：** 12 |
| UDMF\_META\_SCRIPT "general.script" | 所有脚本语言源代码的基类型，归属类型为SOURCE\_CODE。  **起始版本：** 12 |
| UDMF\_META\_SHELL\_SCRIPT "general.shell-script" | Shell脚本类型，归属类型为SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_CSH\_SCRIPT "general.csh-script" | C-shell脚本类型，归属类型为SHELL\_SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_PERL\_SCRIPT "general.perl-script" | Perl脚本类型，归属类型为SHELL\_SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_PHP\_SCRIPT "general.php-script" | PHP脚本类型，归属类型为SHELL\_SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_PYTHON\_SCRIPT "general.python-script" | Python脚本类型，归属类型为SHELL\_SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_RUBY\_SCRIPT "general.ruby-script" | Ruby脚本类型，归属类型为SHELL\_SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_TYPE\_SCRIPT "general.type-script" | TypeScript源代码类型，归属类型为SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_JAVA\_SCRIPT "general.java-script" | JavaScript源代码类型，归属类型为SCRIPT。  **起始版本：** 12 |
| UDMF\_META\_C\_HEADER "general.c-header" | C头文件类型，归属类型为SOURCE\_CODE。  **起始版本：** 12 |
| UDMF\_META\_C\_SOURCE "general.c-source" | C源代码类型，归属类型为SOURCE\_CODE。  **起始版本：** 12 |
| UDMF\_META\_C\_PLUS\_PLUS\_HEADER "general.c-plus-plus-header" | C++头文件类型，归属类型为SOURCE\_CODE。  **起始版本：** 12 |
| UDMF\_META\_C\_PLUS\_PLUS\_SOURCE "general.c-plus-plus-source" | C++源代码类型，归属类型为SOURCE\_CODE。  **起始版本：** 12 |
| UDMF\_META\_JAVA\_SOURCE "general.java-source" | Java源代码类型，归属类型为SOURCE\_CODE。  **起始版本：** 12 |
| UDMF\_META\_EBOOK "general.ebook" | 所有电子书文件格式的基类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_EPUB "general.epub" | 电子出版物（EPUB）文件格式类型，归属类型为EBOOK。  **起始版本：** 12 |
| UDMF\_META\_AZW "com.amazon.azw" | AZW电子书文件格式类型，归属类型为EBOOK。  **起始版本：** 12 |
| UDMF\_META\_AZW3 "com.amazon.azw3" | AZW3电子书文件格式类型，归属类型为EBOOK。  **起始版本：** 12 |
| UDMF\_META\_KFX "com.amazon.kfx" | KFX电子书文件格式类型，归属类型为EBOOK。  **起始版本：** 12 |
| UDMF\_META\_MOBI "com.amazon.mobi" | MOBI电子书文件格式类型，归属类型为EBOOK。  **起始版本：** 12 |
| UDMF\_META\_MEDIA "general.media" | 所有媒体的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_IMAGE "general.image" | 所有图片的基类型，归属类型为MEDIA。  **起始版本：** 12 |
| UDMF\_META\_JPEG "general.jpeg" | JPEG图片类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_PNG "general.png" | PNG图片类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_RAW\_IMAGE "general.raw-image" | 所有原始图像格式的基类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_TIFF "general.tiff" | TIFF图片类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_BMP "com.microsoft.bmp" | WINDOWS位图图像类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_ICO "com.microsoft.ico" | WINDOWS图标图像类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_PHOTOSHOP\_IMAGE "com.adobe.photoshop-image" | Adobe Photoshop图片类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_AI\_IMAGE "com.adobe.illustrator.ai-image" | Adobe Illustrator图片类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_WORD\_DOC "com.microsoft.word.doc" | Microsoft Word数据类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_EXCEL "com.microsoft.excel.xls" | Microsoft Excel数据类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_PPT "com.microsoft.powerpoint.ppt" | Microsoft PowerPoint演示文稿类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_PDF "com.adobe.pdf" | PDF数据类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_POSTSCRIPT "com.adobe.postscript" | PostScript数据类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_ENCAPSULATED\_POSTSCRIPT "com.adobe.encapsulated-postscript" | Encapsulated PostScript类型，归属类型为POSTSCRIPT。  **起始版本：** 12 |
| UDMF\_META\_VIDEO "general.video" | 所有视频的基类型，归属类型为MEDIA。  **起始版本：** 12 |
| UDMF\_META\_AVI "general.avi" | AVI视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_MPEG "general.mpeg" | MPEG-1或MPEG-2视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_MPEG4 "general.mpeg-4" | MPEG-4视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_VIDEO\_3GPP "general.3gpp" | 3GPP视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_VIDEO\_3GPP2 "general.3gpp2" | 3GPP2视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_WINDOWS\_MEDIA\_WM "com.microsoft.windows-media-wm" | WINDOWS WM视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMV "com.microsoft.windows-media-wmv" | WINDOWS WMV视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMP "com.microsoft.windows-media-wmp" | WINDOWS WMP视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_AUDIO "general.audio" | 所有音频的基类型，归属类型为MEDIA。  **起始版本：** 12 |
| UDMF\_META\_AAC "general.aac" | AAC音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_AIFF "general.aiff" | AIFF音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_ALAC "general.alac" | ALAC音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_FLAC "general.flac" | FLAC音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_MP3 "general.mp3" | MP3音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_OGG "general.ogg" | OGG音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_PCM "general.pcm" | PCM音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMA "com.microsoft.windows-media-wma" | WINDOWS WMA音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_WAVEFORM\_AUDIO "com.microsoft.waveform-audio" | WINDOWS波形音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_WINDOWS\_MEDIA\_WMX "com.microsoft.windows-media-wmx" | WINDOWS WMX视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_WINDOWS\_MEDIA\_WVX "com.microsoft.windows-media-wvx" | WINDOWS WVX视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_WINDOWS\_MEDIA\_WAX "com.microsoft.windows-media-wax" | WINDOWS WAX音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_GENERAL\_FILE "general.file" | 所有文件的基类型，归属类型为ENTITY。  **起始版本：** 12 |
| UDMF\_META\_DIRECTORY "general.directory" | 所有目录的基类型，归属类型为ENTITY。  **起始版本：** 12 |
| UDMF\_META\_FOLDER "general.folder" | 所有文件夹的基类型，归属类型为DIRECTORY。  **起始版本：** 12 |
| UDMF\_META\_SYMLINK "general.symlink" | 所有符号链接的基类型，归属类型为ENTITY。  **起始版本：** 12 |
| UDMF\_META\_ARCHIVE "general.archive" | 所有文件和目录存档文件的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_BZ2\_ARCHIVE "general.bz2-archive" | BZ2存档文件类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_DISK\_IMAGE "general.disk-image" | 所有可作为卷装载项的文件类型的基类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_TAR\_ARCHIVE "general.tar-archive" | TAR存档文件类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_ZIP\_ARCHIVE "general.zip-archive" | ZIP存档文件类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_JAVA\_ARCHIVE "com.sun.java-archive" | JAVA存档文件类型，归属类型为ARCHIVE和EXECUTABLE。  **起始版本：** 12 |
| UDMF\_META\_GNU\_TAR\_ARCHIVE "org.gnu.gnu-tar-archive" | GUN存档文件类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_GNU\_ZIP\_ARCHIVE "org.gnu.gnu-zip-archive" | GZIP存档文件类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_GNU\_ZIP\_TAR\_ARCHIVE "org.gnu.gnu-zip-tar-archive" | GZIP TAR存档文件类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_CALENDAR "general.calendar" | 所有日程类数据的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_CONTACT "general.contact" | 所有联系人类数据的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_DATABASE "general.database" | 所有数据库文件的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_MESSAGE "general.message" | 所有消息类数据的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_VCARD "general.vcard" | 所有电子名片类数据的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_NAVIGATION "general.navigation" | 所有导航类数据的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_LOCATION "general.location" | 导航定位类型，归属类型为NAVIGATION。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_FORM "openharmony.form" | 系统定义的卡片类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_APP\_ITEM "openharmony.app-item" | 系统定义的桌面图标类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_PIXEL\_MAP "openharmony.pixel-map" | 系统定义的像素图类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_ATOMIC\_SERVICE "openharmony.atomic-service" | 系统定义的元服务类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_PACKAGE "openharmony.package" | 系统定义的包（即目录的打包文件），归属类型为DIRECTORY。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_HAP "openharmony.hap" | 系统定义的能力包，归属类型为OPENHARMONY\_PACKAGE。  **起始版本：** 12 |
| UDMF\_META\_SMIL "com.real.smil" | 同步多媒体集成语言类型，归属类型为XML文本类型。  **起始版本：** 12 |
| UDMF\_META\_MARKDOWN "general.markdown" | 标记语言文本类型，归属类型为PLAIN\_TEXT。  **起始版本：** 12 |
| UDMF\_META\_FAX "general.fax" | 传真图像的基本类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_JFX\_FAX "com.j2.jfx-fax" | J2 jConnect传真文件类型，归属类型为FAX。  **起始版本：** 12 |
| UDMF\_META\_EFX\_FAX "com.js.efx-fax" | 电子传真文件类型，归属类型为FAX。  **起始版本：** 12 |
| UDMF\_META\_XBITMAP\_IMAGE "general.xbitmap-image" | X Window系统（X11）中使用的位图图像格式，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_TGA\_IMAGE "com.truevision.tga-image" | 标签图形（TaggedGraphics）图像类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_SGI\_IMAGE "com.sgi.sgi-image" | 硅图（Silicon Graphics）图像类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_OPENEXR\_IMAGE "com.ilm.openexr-image" | 开放标准的高动态范围图像格式类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_FLASHPIX\_IMAGE "com.kodak.flashpix.image" | FlashPix图像文件类型，归属类型为IMAGE。  **起始版本：** 12 |
| UDMF\_META\_REALMEDIA "com.real.realmedia" | 流媒体视频类型，归属类型为VIDEO。  **起始版本：** 12 |
| UDMF\_META\_AU\_AUDIO "general.au-audio" | Au数据格式，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_AIFC\_AUDIO "general.aifc-audio" | 音频交换数据类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_SD2\_AUDIO "com.digidesign.sd2-audio" | 单声道/立体声音频类型（Digidesign Sound Designer II），归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_REALAUDIO "com.real.realaudio" | RealMedia音频类型，归属类型为AUDIO。  **起始版本：** 12 |
| UDMF\_META\_OPENXML "org.openxmlformats.openxml" | 开源XML基类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_WORDPROCESSINGML\_DOCUMENT "org.openxmlformats.wordprocessingml.document" | 开源XML文档类型，归属类型为OPENXML和COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_SPREADSHEETML\_SHEET "org.openxmlformats.spreadsheetml.sheet" | 开源XML电子表格类型，归属类型为OPENXML和COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_PRESENTATIONML\_PRESENTATION "org.openxmlformats.presentationml.presentation" | 开源XML演示文稿类型，归属类型为OPENXML和COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENDOCUMENT "org.oasis.opendocument" | Office应用程序的开源文档类型，归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_OPENDOCUMENT\_TEXT "org.oasis.opendocument.text" | 开源文档类型，归属类型为OPENDOCUMENT和COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENDOCUMENT\_SPREADSHEET "org.oasis.opendocument.spreadsheet" | 开源文档电子表格类型，归属类型为OPENDOCUMENT和COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENDOCUMENT\_PRESENTATION "org.oasis.opendocument.presentation" | 开源文档演示类型，归属类型为OPENDOCUMENT和COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENDOCUMENT\_GRAPHICS "org.oasis.opendocument.graphics" | 开源文档图形类型，归属类型为OPENDOCUMENT和COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENDOCUMENT\_FORMULA "org.oasis.opendocument.formula" | 开源文档公式集类型，归属类型为OPENDOCUMENT。  **起始版本：** 12 |
| UDMF\_META\_STUFFIT\_ARCHIVE "com.allume.stuffit-archive" | Stuffit压缩格式类型（Stuffit archive），归属类型为ARCHIVE。  **起始版本：** 12 |
| UDMF\_META\_VCS "general.vcs" | VCalendar日历数据类型，归属类型为CALENDAR和TEXT。  **起始版本：** 12 |
| UDMF\_META\_ICS "general.ics" | ICalendar日历数据类型，归属类型为CALENDAR和TEXT。  **起始版本：** 12 |
| UDMF\_META\_EXECUTABLE "general.executable" | 所有可执行文件的基类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_PORTABLE\_EXECUTABLE "com.microsoft.portable-executable" | Microsoft Windows应用程序类型，归属类型为EXECUTABLE。  **起始版本：** 12 |
| UDMF\_META\_SUN\_JAVA\_CLASS "com.sun.java-class" | Java类文件类型，归属类型为EXECUTABLE。  **起始版本：** 12 |
| UDMF\_META\_FONT "general.font" | 所有字体数据类型的基础类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_TRUETYPE\_FONT "general.truetype-font" | TrueType字体类型，归属类型为FONT。  **起始版本：** 12 |
| UDMF\_META\_TRUETYPE\_COLLECTION\_FONT "general.truetype-collection-font" | TrueType collection字体类型，归属类型为FONT。  **起始版本：** 12 |
| UDMF\_META\_OPENTYPE\_FONT "general.opentype-font" | OpenType字体类型，归属类型为FONT。  **起始版本：** 12 |
| UDMF\_META\_POSTSCRIPT\_FONT "com.adobe.postscript-font" | PostScript字体类型，归属类型为FONT。  **起始版本：** 12 |
| UDMF\_META\_POSTSCRIPT\_PFB\_FONT "com.adobe.postscript-pfb-font" | PostScript Font Binary字体类型，归属类型为FONT。  **起始版本：** 12 |
| UDMF\_META\_POSTSCRIPT\_PFA\_FONT "com.adobe.postscript-pfa-font" | Adobe Type 1 字体类型，归属类型为FONT。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_HDOC "openharmony.hdoc" | 系统定义的备忘录数据类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_HINOTE "openharmony.hinote" | 系统定义的笔记数据类型，归属类型为COMPOSITE\_OBJECT。 |
| UDMF\_META\_OPENHARMONY\_STYLED\_STRING "openharmony.styled-string" | 系统定义的样式字符串类型，归属类型为COMPOSITE\_OBJECT。  **起始版本：** 12 |
| UDMF\_META\_OPENHARMONY\_WANT "openharmony.want" | 系统定义的Want类型，归属类型为OBJECT。  **起始版本：** 12 |
| UDMF\_META\_GENERAL\_FILE\_URI "general.file-uri" | 文件地址类型，归属类型为TEXT。  **起始版本：** 13 |
| UDMF\_METE\_GENERAL\_CONTENT\_FORM "general.content-form" | 内容卡片类型，归属类型为OBJECT。  **起始版本：** 14 |
