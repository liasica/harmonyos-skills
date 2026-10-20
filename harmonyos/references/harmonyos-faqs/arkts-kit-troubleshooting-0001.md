---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-troubleshooting-0001
title: 页面上展示的日期与实际时间不符
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 故障排查 > 页面上展示的日期与实际时间不符
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:19+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:94f460791a98b982ee4cf81de72659976d31ab9803cd248d70f8339fab4f9eb0
---

## 问题现象

应用中展示的当前时间中，月份比当前系统时间的月份小1。例如，当前系统时间为2025年7月25日。应用中展示的当前时间是2025年6月25日。

问题代码为：

```ts
// ...
@State newTime: string = '';

// ...
const nowTime = new Date();
nowTime.toDateString();
const nowYear = nowTime.getFullYear();
const nowMonth = nowTime.getMonth();
const nowDate = nowTime.getDate();
this.newTime = ((((nowYear + "年") + nowMonth) + "月") + nowDate) + "日";
// ...
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/WChPIpn2Rjmj0gTmpUm1Rw/zh-cn_image_0000002766015488.png "点击放大")

## 定位过程

检查代码，可以发现对于日期的处理采用了拼接的方式，且月份直接通过getMonth()获取。

## 分析结论

Date.getMonth()，其获取的月份从0开始，没有做加1处理，导致实际展示的月份比实际月份小1。

## 修改建议

* 自拼接处理需要在月份上做加1处理。
* 推荐使用时间日期国际化，对时间日期格式化处理。同时，还可以根据不同的国家，进行针对性的格式化处理满足国际化的需求。

示例代码为：

```ts
@Entry
@Component
struct ThisTime {
  @State newTime: string = '拼接处理的时间：';
  @State formatDate: string = '格式化处理的时间：';

  build() {
    Column({ space: 20 }) {
      Column() {
        Button('自拼接处理').onClick(() => {
          const nowTime = new Date();
          nowTime.toDateString();
          const nowYear = nowTime.getFullYear();
          const nowMonth = nowTime.getMonth() + 1;
          const nowDate = nowTime.getDate();
          this.newTime = ((((nowYear + '年') + nowMonth) + '月') + nowDate) + '日';
        });

        Button('推荐使用时间日期国际化').onClick(() => {
          const date = new Date();
          // 创建DateTimeFormat对象
          let fullFormat: Intl.DateTimeFormat =
            new Intl.DateTimeFormat('zh-CN', { dateStyle: 'full', timeStyle: 'full' });
          let formattedDate: string = fullFormat.format(date);
          this.newTime =
            '拼接处理的时间（月份需要+1）：' + date.getFullYear() + '年' + (date.getMonth() + 1) + '月' + date.getDate() +
              '日';
          this.formatDate = '格式化处理的时间：' + formattedDate;
        });
        Text(this.newTime);
        Text(this.formatDate);
      };
    }.width('100%').alignItems(HorizontalAlign.Center);
  }
}
```
