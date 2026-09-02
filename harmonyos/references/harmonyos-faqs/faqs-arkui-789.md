---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-789
title: 上传的自定义字体无法正确加载
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 上传的自定义字体无法正确加载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:9e4d4379a9e8a10170cce150a9c67b622ffec8bbda17e25dcebbeea225e52ff8
---

## 问题现象

利用picker选择ttf格式的字体导入到手机沙箱目录后，利用registerFont方法无法成功加载，关键问题代码如下：

```ts
import fs from '@ohos.file.fs';
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
import picker from '@ohos.file.picker';

@Entry
@Component
struct FontManager {
  @State isImporting: boolean = false;
  @State fontList: string[] = ['HarmonyOS Sans', 'HarmonyHeiTi', 'SourceHanSans'];
  @State selectedFont: string = 'HarmonyOS Sans';
  @State showDropdown: boolean = false;
  @State uploadProgress: number = 0;
  @State fontFamily: string = '';
  @State filePath: string = '';

  build() {
    Column({ space: 10 }) {
      // 字体选择区域
      this.buildFontSelector();

      // 字体导入按钮
      this.buildImportButton();

      // 上传进度条（只在导入时显示）
      if (this.isImporting) {
        this.buildProgressBar();
      }
    }
    .width('100%')
    .padding(10);
  }

  @Builder
  buildFontSelector() {
    Column() {
      // 当前选中字体显示
      Row({ space: 8 }) {
        Text(this.selectedFont)
          .fontSize(14)
          .fontColor('#333333')
          .fontFamily(this.selectedFont);

        Image($r('app.media.startIcon'))
          .width(12)
          .height(12)
          .fillColor('#999999');
      }
      .width('100%')
      .height(40)
      .padding({ left: 12, right: 12 })
      .backgroundColor('#FFFFFF')
      .border({ width: 1, color: '#E8E8E8', radius: 4 })
      .onClick(() => {
        this.showDropdown = !this.showDropdown;
      });

      // 下拉选项
      if (this.showDropdown) {
        Column() {
          ForEach(this.fontList, (font: string) => {
            Row() {
              Text(font)
                .fontSize(14)
                .fontColor('#333333')
                .fontFamily(font)
                .textOverflow({ overflow: TextOverflow.Ellipsis });

              if (this.selectedFont === font) {
                Image($r('app.media.startIcon'))
                  .width(16)
                  .height(16)
                  .margin({ left: 8 });
              }
            }
            .width('100%')
            .height(40)
            .padding({ left: 12, right: 12 })
            .backgroundColor('#FFFFFF')
            .onClick(() => {
              this.selectedFont = font;
              this.showDropdown = false;
              // 字体切换回调
              this.onFontChanged(font);
            });
          }, (font: string) => font);
        }
        .width('100%')
        .height(200)
        .backgroundColor('#FFFFFF')
        .border({ width: 1, color: '#E8E8E8', radius: 4 })
        .margin({ top: 4 })
        .clip(true);
      }
    };
  }

  @Builder
  buildImportButton() {
    Row() {
      Text('导入字体')
        .fontColor('#4A90E2')
        .fontSize(14)
        .fontWeight(400)
        .fontFamily('HarmonyHeiTi-medium')
        .textAlign(TextAlign.End)
        .padding({ top: 5, bottom: 10 })
        .width('100%')
        .onClick(() => {
          if (!this.isImporting) {
            this.importFontFile();
          }
        });
    };
  }

  @Builder
  buildProgressBar() {
    Column({ space: 8 }) {
      Text(`上传中... ${this.uploadProgress}%`)
        .fontSize(12)
        .fontColor('#666666');

      Row() {
        Column() {
        }
        .width(`${this.uploadProgress}%`)
        .height(4)
        .backgroundColor('#4A90E2');
      }
      .width('100%')
      .height(4)
      .backgroundColor('#E8E8E8')
      .borderRadius(2);
    }
    .width('100%')
    .padding({ top: 8, bottom: 8 });
  }

  // 导入字体文件
  private async importFontFile() {
    try {
      this.isImporting = true;
      this.uploadProgress = 0;

      // 选择文件
      const documentSelectOptions = new picker.DocumentSelectOptions();
      documentSelectOptions.fileSuffixFilters = ['.ttf', '.otf'];
      const documentViewPicker = new picker.DocumentViewPicker();
      const uris = await documentViewPicker.select(documentSelectOptions);

      this.uploadProgress = 30;

      if (uris && uris.length > 0) {
        const selectedUri = uris[0];
        console.info('原始URI:', selectedUri);
        console.info('解码后URI:', decodeURIComponent(selectedUri));

        // 获取字体名称（包含中文解码）
        this.uploadProgress = 50;
        const fontName = await this.getFontFamilyNameSimple(selectedUri);
        console.info('最终字体名称:', fontName);

        // 复制文件
        this.uploadProgress = 60;
        const fontDir = this.getFontDirectory();
        const fileName = selectedUri.split('/').pop() || 'custom_font.ttf';
        const destPath = `${fontDir}/${fileName}`;
        console.info(`字体路径: ${destPath}`);
        await this.copyFontFile(selectedUri, destPath);

        // 更新字体列表
        this.uploadProgress = 90;
        if (!this.fontList.includes(fontName)) {
          this.fontList = this.fontList.concat([fontName]);
        }

        // 完成
        this.uploadProgress = 100;
        setTimeout(() => {
          this.isImporting = false;
          this.uploadProgress = 0;

          this.getUIContext().getPromptAction().showToast({
            message: `字体 "${fontName}" 导入成功`,
            duration: 2000 // 显示时长（毫秒）
          });
          this.getUIContext().getFont().registerFont({
            familyName: fontName,
            familySrc: `file://${destPath}`
          });
          this.selectedFont = fontName;
          this.onFontChanged(fontName);
        }, 500);
      }

    } catch (error) {
      console.error('导入字体失败:', error);
      this.getUIContext().getPromptAction().showToast({
        message: `导入失败: ${error.message || '未知错误'}`,
        duration: 3000
      });
      this.isImporting = false;
      this.uploadProgress = 0;
    }
  }

  private async getFontFamilyNameSimple(fileUri: string): Promise<string> {
    try {
      // 解码文件URI（如果包含中文）
      const decodedUri = decodeURIComponent(fileUri);

      // 提取文件名
      const fileName = decodedUri.split('/').pop() || '';

      // 如果文件名还是编码格式，再次解码
      let fontName = fileName;
      if (fileName.includes('%')) {
        try {
          fontName = decodeURIComponent(fileName);
        } catch (e) {
          // 如果解码失败，使用原始文件名
          console.warn('解码文件名失败:', e);
        }
      }

      // 移除扩展名并进行清理
      fontName = fontName.replace(/\.(ttf|otf|TTF|OTF)$/, '');
      fontName = this.cleanFontName(fontName);

      return fontName;

    } catch (error) {
      console.error('处理字体名称失败:', error);
      return 'Custom Font';
    }
  }

  private cleanFontName(fontName: string): string {
    if (!fontName) {
      return 'Custom Font';
    }

    // 1.解码URL编码
    let cleaned = fontName;
    if (fontName.includes('%')) {
      try {
        cleaned = decodeURIComponent(fontName);
      } catch (e) {
        console.warn('URL解码失败，使用原名称');
      }
    }

    // 2.移除文件扩展名
    cleaned = cleaned.replace(/\.(ttf|otf|TTF|OTF|ttc|TTC)$/i, '');

    // 3.替换常见分隔符
    cleaned = cleaned
      .replace(/[+_\-]/g, ' ')
      .replace(/\./g, ' ')
      .replace(/\s+/g, ' ')
      .trim();

    // 4.移除常见英文后缀（保留中文）
    const englishSuffixes = [
      'Regular', 'Bold', 'Italic', 'Light', 'Medium',
      'Heavy', 'Black', 'Thin', 'Normal', 'Roman',
      'Oblique', 'Condensed', 'Extended', 'Pro', 'Std',
      'SC', 'TC', 'HC', 'J', 'K', 'R', 'W', 'Extra'
    ];

    englishSuffixes.forEach(suffix => {
      const regex = new RegExp(`\\s*${suffix}\\s*`, 'gi');
      cleaned = cleaned.replace(regex, ' ');
    });

    // 5.移除版本号和数字
    cleaned = cleaned
      .replace(/\s*v?\d+(\.\d+)*\s*/gi, ' ')  // 版本号
      .replace(/\s*\d{2,4}\s*/g, ' ')         // 年份等数字
      .replace(/\s+/g, ' ')                   // 再次合并空格
      .trim();

    // 6.智能处理中英文混合名称
    // 如果包含中文，保留整个名称
    const hasChinese = /[\u4e00-\u9fa5]/.test(cleaned);
    if (hasChinese) {
      // 移除中文名称前后的英文单词
      cleaned = cleaned.replace(/^[A-Za-z\s]+\s+([\u4e00-\u9fa5])/, '$1');
      return cleaned;
    }

    // 7.对于纯英文名称，进行驼峰转换和首字母大写
    cleaned = cleaned
      .replace(/([a-z])([A-Z])/g, '$1 $2')      // 驼峰转空格
      .replace(/([A-Z]+)([A-Z][a-z])/g, '$1 $2') // 连续大写
      .replace(/\b\w/g, (char: string) => char.toUpperCase()) // 首字母大写
      .replace(/\s+/g, ' ')
      .trim();

    return cleaned || 'Custom Font';
  }

  // 获取字体存储目录
  private getFontDirectory(): string {
    const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const filesDir = context.filesDir;
    const fontDir = `${filesDir}/fonts`;

    // 创建字体目录（如果不存在）
    if (!fs.accessSync(fontDir)) {
      fs.mkdirSync(fontDir);
    }

    return fontDir;
  }

  // 修改copyFontFile方法，处理可能的错误
  private async copyFontFile(sourceUri: string, destPath: string): Promise<void> {
    return new Promise((resolve, reject) => {
      try {
        console.info('开始复制文件:', sourceUri, '->', destPath);

        // 打开源文件
        const sourceFile = fs.openSync(sourceUri, fs.OpenMode.READ_ONLY);
        console.info('源文件打开成功');

        // 创建目标文件
        const destFile = fs.openSync(destPath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
        console.info('目标文件创建成功');

        const buffer = new ArrayBuffer(8192);
        let bytesRead = 0;
        let totalBytes = 0;

        while ((bytesRead = fs.readSync(sourceFile.fd, buffer)) > 0) {
          fs.writeSync(destFile.fd, buffer, { offset: 0, length: bytesRead });
          totalBytes += bytesRead;
        }
        console.info('文件复制完成，总字节数:', totalBytes);
        fs.closeSync(sourceFile);
        fs.closeSync(destFile);

        // 验证文件是否成功复制
        if (fs.accessSync(destPath)) {
          const stat = fs.statSync(destPath);
          console.info('目标文件大小:', stat.size, '字节');
          if (stat.size > 0) {
            resolve();
          } else {
            reject(new Error('复制后文件大小为0'));
          }
        } else {
          reject(new Error('复制后文件不存在'));
        }
      } catch (error) {
        console.error('复制文件时出错:', error);
        reject(error);
      }
    });
  }

  // 字体切换回调
  private onFontChanged(fontName: string) {
    console.info('字体已切换为:', fontName);
    this.fontFamily = fontName;
  }

  // 组件初始化时加载已导入的字体
  aboutToAppear() {
    this.loadImportedFonts();
  }

  private loadImportedFonts(): void {
    try {
      const fontDir: string = this.getFontDirectory();
      console.info('字体目录:', fontDir);
      // 确保目录存在
      if (!fs.accessSync(fontDir)) {
        fs.mkdirSync(fontDir, true);
        console.info('创建字体目录成功:', fontDir);
      }
      // 列出所有文件
      let allFiles: string[] = [];
      try {
        allFiles = fs.listFileSync(fontDir);
        console.info('找到文件列表:', allFiles);
      } catch (listError) {
        console.warn('列出文件失败，可能目录为空:', listError);
        allFiles = [];
      }
      // 更新字体列表
      const importedFonts: string[] = [];
      allFiles.forEach((fileName: string) => {
        console.info('更新字体列表');
        console.info(fileName);
        const decodedUri = decodeURIComponent(fileName);
        // 提取文件名
        const newName = decodedUri.split('/').pop() || '';
        if (/\.(ttf|otf|TTF|OTF)$/.test(newName)) {
          let fontName = newName.replace(/\.(ttf|otf|TTF|OTF)$/, '');
          fontName = this.cleanFontName(fontName);
          const fontPath = fontDir + '/' + fileName;
          try {
            if (fs.accessSync(fontPath)) {
              console.info(`[调试] 字体文件存在。`);
            }
          } catch (e) {
            console.error(`[调试] 字体文件不存在或不可访问！`);
            return; // 直接返回，避免注册
          }
          try {
            this.getUIContext().getFont().registerFont({
              familyName: fontName,
              familySrc: `file://${fontPath}`
            });
          } catch (error) {
            const err = error as BusinessError;
            // 如果字体已注册或其他错误，这里可以选择静默失败或使用默认字体
            console.error(`Failed to register font. Code: ${err.code}, Message: ${err.message}`);
          }
          importedFonts.push(fontName);
        }
      });
      console.info('找到导入的字体:', importedFonts);
      // 合并字体列表，避免重复
      const allFonts = this.fontList.concat(importedFonts)
        .filter((value, index, array) => array.indexOf(value) === index);
      this.fontList = allFonts;
    } catch (error) {
      console.error('加载字体列表失败:', error);
    }
  }
}
```

## 背景知识

* [@ohos.file.picker (选择器)](../harmonyos-references/js-apis-file-picker.md)：选择器是一个封装DocumentViewPicker、AudioViewPicker、PhotoViewPicker的API模块，具有选择与保存的能力。
* [fs.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync)：以同步方法将数据写入文件。
* [registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)：在字体管理中注册自定义字体。

## 问题定位

1. 首先观察问题代码，发现不仅仅有上传后加载自定义字体功能，在aboutToAppear方法中还存在加载沙箱字体的功能，于是尝试在沙箱目录直接传入自定义字体，发现字体加载正常，故可以确定问题出现在文件上传方法处。
2. 然后选择自定义文件进行上传，观察Device File Browser内的上传文件，发现其大小只有8KB，小于正常字体大小，故可以确定文件上传不完整。
3. 根据打印日志内容，发现上传后其字节数小于上传前的字节数，故可以断定问题出现fs.writeSync上。
4. 发现fs.writeSync的参数offset一直为0，所以循环时每次都会覆盖之前的内容，最终导致文件不完整。

## 分析结论

fs.writeSync文件写入时参数设置错误导致文件拷贝失败，从而无法正确注册自定义字体。

## 修改建议

问题代码fs.writeSync(destFile.fd, buffer, { offset: 0, length: bytesRead })修改成fs.writeSync(destFile.fd, buffer, { offset: totalBytes, length: bytesRead })即可。
