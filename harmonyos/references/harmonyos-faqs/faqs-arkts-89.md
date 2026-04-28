---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-89
title: 如何将JSON对象转换成HashMap
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将JSON对象转换成HashMap
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fa4725f70967a4118193862ad9aa082129c05c92b2f03c60b97c6a3211097ba8
---

可以参考如下示例代码：

```
1. import { HashMap } from '@kit.ArkTS';

3. let str: string = '{\"common_params\": {' +
4. '\"city_id\": 1,' +
5. '\"nav_id_list\": \"\",' +
6. '\"show_hook_card\": 2,' +
7. '\"use_one_stop_structure\": 1,' +
8. '\"version_tag\": \"homepageonestop\"' +
9. '}' +
10. '}';

12. let jsonObj: Object = JSON.parse(str);
13. let commObj = (jsonObj as Record<string, Object>);
14. let commRecord = (commObj['common_params'] as Record<string, Object>);
15. let keyStr = Object.keys(commRecord);

17. for (let index: number = 0; index < keyStr.length; index++) {
18. commRecord[keyStr[index].toString()].toString();
19. }

21. let hashMapData: HashMap<string, Object> = new HashMap();
22. hashMapData.set('common_params', commRecord);

24. @Entry
25. @Component
26. struct Index {
27. build() {
28. Row() {
29. Column() {
30. Button('JSON to HashMap')
31. .onClick(() => {
32. // common_params: {"city_id":1,"nav_id_list":"","show_hook_card":2,"use_one_stop_structure":1,"version_tag":"homepageonestop"}
33. console.log('common_params:', JSON.stringify(hashMapData.get('common_params')));
34. })
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
```

[HashMapFile.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/HashMapFile.ets#L21-L60)
