---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1395
title: 使用TextPicker实现DatePicker的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用TextPicker实现DatePicker的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ed9cdfe7c812a6fe41957d8c4ba67f6cc2b6306c2a396d9dbf9bbd2026051fa1
---

## 问题现象

DatePicker可以用于在指定日期范围内选择日期，但是开发过程中DatePicker的样式或者功能往往不能够满足自定义需求，如以下场景：

* 场景一：DatePicker滑动过程中，年月日的滚动会互相关联，比如选择2025年12月，从12月滚动到1月时，年份会变成2026年，无法满足自定义要求。
* 场景二：DatePicker只能选择年月日，无法满足只有【年】或者【年月】或【月日】的场景。
* 场景三：实现只有【年月】的生日选择器，要求切换年份时月份变为与原来选择月份的最近月份。

## 背景知识

* [DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)：日期选择器，用于根据指定日期范围创建日期滑动选择器。滚动时年月会自动关联。
* [TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)：滑动选择文本内容的组件。可以按需创建单列数据选择器、多列非联动数据选择器和多列联动数据选择器。

## 解决方案

* 场景一解决方案：使用多列非联动数据选择器。可以给TextPicker多列分别设置为年和月，即可模拟DatePicker日期选择效果。

  ```ts
  @Entry
  @Component
  struct TextPickerExample1 {
    private years: string[] =
      ['2015年', '2016年', '2017年', '2018年', '2019年', '2020年', '2021年', '2022年', '2023年',
        '2024年', '2025年', '2026年', '2027年', '2028年', '2029年', '2030年'];
    private months: string[] = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
    private multi: string[][] = [this.years, this.months];

    build() {
      Column() {
        TextPicker({ range: this.multi })
          .onChange((value: string | string[], index: number | number[]) => {
            console.info(`TextPicker 多列:onChange ${JSON.stringify(value)} , index: ${JSON.stringify(index)}`);
          }).margin({ top: 250 });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/cU5-8QDYTu-7fZKtEWswYw/zh-cn_image_0000002628762570.png "点击放大")

* 场景二解决方案：使用单列联动选择器实现年的选择，多列联动选择器实现年月或月日的选择。

  ```ts
  @Entry
  @Component
  struct TextPickerExample2 {
    @State generateYearMonth: TextCascadePickerRangeContent [] = [];
    @State generateMonthDay: TextCascadePickerRangeContent [] = [];
    @State generateYear: TextCascadePickerRangeContent [] = [];

    generateYearMonthRange(startYear: number, endYear: number): TextCascadePickerRangeContent[] {
      const range: TextCascadePickerRangeContent[] = [];
      for (let year = startYear; year <= endYear; year++) {
        const months: TextCascadePickerRangeContent[] = [];
        for (let month = 1; month <= 12; month++) {
          months.push({
            text: `${month.toString().padStart(2, '0')}月` // 确保月份是两位数
          });
        }
        // 只有当月份数组不为空时，才添加到range中
        if (months.length > 0) {
          range.push({
            text: `${year}年`, // 使用年份作为文本
            children: months // 只有当月份不为空时，才设置children属性
          });
        }
      }
      return range; // 返回一维数组
    }

    generateMonthDayRange(year: number): TextCascadePickerRangeContent[] {
      const range: TextCascadePickerRangeContent[] = [];
      // 生成月份
      for (let month = 1; month <= 12; month++) {
        const days: TextCascadePickerRangeContent[] = [];
        // 计算每个月的天数
        let daysInMonth = new Date(year, month, 0).getDate();
        for (let day = 1; day <= daysInMonth; day++) {
          days.push({
            text: `${day.toString().padStart(2, '0')}日` // 确保天数是两位数
          });
        }
        range.push({
          text: `${month.toString().padStart(2, '0')}月`, // 使用月份作为文本
          children: days
        });
      }
      return range;
    }

    generateYearRange(startYear: number, endYear: number): TextCascadePickerRangeContent[] {
      const range: TextCascadePickerRangeContent[] = [];
      for (let year = startYear; year <= endYear; year++) {
        range.push({
          text: `${year}年`
        });
      }
      return range;
    }

    aboutToAppear(): void {
      this.generateYear = this.generateYearRange(2000, 2025);
      this.generateYearMonth = this.generateYearMonthRange(2000, 2025);
      this.generateMonthDay = this.generateMonthDayRange(2025);
    }

    build() {
      Column() {
        Button('指定【年】区间列表');
        TextPicker({ range: this.generateYear });
        Button('指定【年】【月】区间列表');
        TextPicker({ range: this.generateYearMonth });
        Button('【月】【日】区间列表');
        TextPicker({ range: this.generateMonthDay });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/9cc7KtmHQheisHaOMTW6bA/zh-cn_image_0000002658961883.png "点击放大")

* 场景三解决方案：当多列联动选择器触发[onChange](../harmonyos-references/ts-basic-components-textpicker.md#onchange18)时，判断如果年份发生改变，就把月份设置为之前的月。

  ```ts
  @Entry
  @Component
  struct TextPickerExample3 {
    @State generateYearMonth: TextCascadePickerRangeContent [] = [];
    curYear: number = 0;
    curMonth: number = 0;
    @State curYearIndex: number = 0;
    @State curMonthIndex: number = 0;

    generateYearMonthRange(startYear: number, endYear: number): TextCascadePickerRangeContent[] {
      const range: TextCascadePickerRangeContent[] = [];
      for (let year = startYear; year <= endYear; year++) {
        const months: TextCascadePickerRangeContent[] = [];
        for (let month = 1; month <= (year !== endYear ? 12 : this.curMonth); month++) {
          months.push({
            text: `${month.toString().padStart(2, '0')}月` // 确保月份是两位数
          });
        }
        // 只有当月份数组不为空时，才添加到range中
        if (months.length > 0) {
          range.push({
            text: `${year}年`, // 使用年份作为文本
            children: months // 只有当月份不为空时，才设置children属性
          });
        }
      }
      return range; // 多列联动数据
    }

    aboutToAppear(): void {
      // 创建当前日期对象
      const currentDate: Date = new Date();
      // 获取当前月份（注意：月份从0开始，0=1月，11=12月）
      this.curYear = currentDate.getFullYear();
      this.curMonth = currentDate.getMonth() + 1;
      // 生成2000年-当前时间的【年月】日历
      this.generateYearMonth = this.generateYearMonthRange(2000, this.curYear);
    }

    build() {
      Column() {
        TextPicker({ range: this.generateYearMonth })
          .selectedIndex([this.curYearIndex, this.curMonthIndex])
          .onChange((value: string | string[], index: number | number[]) => {
            console.info(`TextPicker 多列:onChange ${value}, index: ${index}`);
            if (this.curYearIndex === (index as number[])[0]) {
              // 改变月份时更新当前选择的月份索引值
              this.curMonthIndex = (index as number[])[1];
            } else {
              // 改变年份时更新当前选择的年份索引值
              this.curYearIndex = (index as number[])[0];
              // 获取当前选择年份的月份列表长度
              let monthLength: number = this.generateYearMonth[this.curYearIndex].children!.length;
              // 更新选择的月份索引值
              // 例如原先选择的2024年9月，改变年份为2025年后月份只有1-8月，则月份默认值修改为距离最近的8月
              // 例如原先选择的2024年5月改变年份为2025年后，则月份索引值保持原来选择的5月
              this.curMonthIndex = this.curMonthIndex > monthLength - 1 ? monthLength - 1 : this.curMonthIndex;
            }
          })
          .margin({ top: 250 })
          .canLoop(false);
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ogdDIe6gRtWc4BqF_v5AJg/zh-cn_image_0000002628602672.png "点击放大")
