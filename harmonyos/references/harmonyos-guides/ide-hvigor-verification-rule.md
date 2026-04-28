---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-verification-rule
title: HAP唯一性校验逻辑
breadcrumb: 指南 > 构建应用 > 配置构建流程 > HAP唯一性校验逻辑
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a10e2cecbcec39fae8536985b903c0e2b9058b8fa579f78b6b48b8696516d20d
---

HAP是应用安装的基本单位，在DevEco Studio工程目录中，一个HAP对应一个Module。应用打包时，每个Module生成一个.hap文件。

应用如果包含多个Module，在应用市场上架时，会将多个.hap文件打包成一个.app文件（称为Bundle），但在云端分发和端侧安装时，仍然是以HAP为基本单位。

为了能够正常分发和安装应用，需要保证一个应用安装到设备时，Module的名称、Ability的名称不重复，并且只有一个Entry类型的Module与目标设备相对应。

DevEco Studio会在编译构建时，对HAP进行上述唯一性校验，如果校验不通过，将会编译失败或给出告警。

## Module校验逻辑

校验目的：同一目标设备上Module唯一。

1. 校验Module的Name。如果多个Module的Name不同，则校验通过。如果Name相同，继续校验deviceType。
2. 校验设备类型deviceType。如果deviceType不相交，则校验通过。如果deviceType相交，继续校验distributionFilter。

   deviceType不相交是指两个Module的deviceType中配置了完全不同的设备，例如：

   ```
   1. //Module1和Module2配置了完全不同的设备，deviceType不相交。
   2. //Module1
   3. {
   4. "deviceType": ["tv", "tablet"]
   5. }
   6. //Module2
   7. {
   8. "deviceType": ["car"]
   9. }
   ```

   deviceType相交是指两个Module的deviceType中包含了相同的设备，例如：

   ```
   1. //Module1和Module2因为都包含"tablet"设备，导致deviceType相交。
   2. //Module1
   3. {
   4. "deviceType": ["tv", "tablet"]
   5. }
   6. //Module2
   7. {
   8. "deviceType": ["car", "tablet"]
   9. }
   ```
3. 校验分发规则distributionFilter。如果distributionFilter不相交，则校验通过。如果distributionFilter相交，则无法保证Module唯一性，校验失败，打包失败。

   distributionFilter中包含属性apiVersion、screenShape、screenWindow、screenDensity和countryCode。相交的相关含义如下：

   * distributionFilter不相交：如果两个distributionFilter中任意一个属性不相交，则两个distributionFilter不相交。
   * distributionFilter相交：如果两个distributionFilter中所有属性都相交，则两个distributionFilter相交。

   例如，两 Module 中的apiVersion、screenShape、screenWindow、screenDensity都相交，但countryCode不相交，则可以区分两个Module，校验通过。

   ```
   1. //Module1和Module2的两个distributionFilter中，countryCode不相交，则两个distributionFilter不相交。
   2. //Module1
   3. {
   4. "distributionFilter": {
   5. "apiVersion" : {
   6. "policy": "include",
   7. "value": [10,11]
   8. },
   9. "screenShape": {
   10. "policy": "include",
   11. "value": ["rect"]
   12. },
   13. "screenWindow": {
   14. "policy": "include",
   15. "value": ["454*454", "466*466"]
   16. },
   17. "screenDensity": {
   18. "policy": "include",
   19. "value": ["ldpi", "xldpi"]
   20. },
   21. "countryCode": {
   22. "policy": "include",
   23. "value": ["CN", "HK"]
   24. }
   25. }
   26. }
   27. //Module2
   28. {
   29. "distributionFilter": {
   30. "apiVersion" : {
   31. "policy": "include",
   32. "value": [10,11]
   33. },
   34. "screenShape": {
   35. "policy": "include",
   36. "value": ["rect"]
   37. },
   38. "screenWindow": {
   39. "policy": "include",
   40. "value": ["454*454", "466*466"]
   41. },
   42. "screenDensity": {
   43. "policy": "include",
   44. "value": ["ldpi", "xldpi"]
   45. },
   46. "countryCode": {
   47. "policy": "include",
   48. "value": ["USA", "UK"]
   49. }
   50. }
   51. }
   ```

## Ability校验逻辑

校验目的：同一目标设备上Ability唯一。

1. 校验Ability的Name。如果多个Ability的Name不同，则校验通过。如果Name相同，继续校验Ability所属Module的deviceType。
2. 校验Ability所属Module的deviceType。如果deviceType不相交，校验通过。如果deviceType相交，继续校验Ability所属Module的distributionFilter。

   例如，两个Ability的Name相同，但其所属Module的deviceType不相交，校验通过。

   ```
   1. //Ability1和Ability2虽然名称相同，但由于其所属Module的deviceType不相交，所以可以区分两个Ability，校验通过。
   2. //Ability1
   3. {
   4. "module": {
   5. "name": "module_sample1",
   6. "deviceType": ["tv", "tablet"],
   7. "abilities": [
   8. {
   9. "name": "ability_sample"
   10. }
   11. ]
   12. }
   13. }
   14. //Ability2
   15. {
   16. "module": {
   17. "name": "module_sample2",
   18. "deviceType": ["car"],
   19. "abilities": [
   20. {
   21. "name": "ability_sample"
   22. }
   23. ]
   24. }
   25. }
   ```
3. 校验Ability所属Module的distributionFilter。如果distributionFilter不相交，校验通过。如果distributionFilter相交，校验失败，抛出告警。

   例如，两个Ability的Name相同，其所属Module的deviceType也相交，但其所属Module的distributionFilter不相交，校验通过。

   ```
   1. //Ability1和Ability2的Name相同，而且其所属Module的deviceType相交，但其所属Module的distributionFilter不相交，所以可以区分两个Ability，校验通过。
   2. //Ability1
   3. {
   4. "module": {
   5. "name": "module_sample",
   6. "deviceType": ["tv", "tablet"],
   7. "metadata": [
   8. {
   9. "name": "distributionFilter_config",
   10. "resource": "$profile:distributionFilter_config_sample1"
   11. }
   12. ],
   13. "abilities": [
   14. {
   15. "name": "ability_sample"
   16. }
   17. ]
   18. }
   19. }
   20. //Ability1所属Module的distributionFilter
   21. {
   22. "distributionFilter": {
   23. "apiVersion" : {
   24. "policy": "include",
   25. "value": [10,11]
   26. },
   27. "screenShape": {
   28. "policy": "include",
   29. "value": ["rect"]
   30. },
   31. "screenWindow": {
   32. "policy": "include",
   33. "value": ["454*454", "466*466"]
   34. },
   35. "screenDensity": {
   36. "policy": "include",
   37. "value": ["ldpi", "xldpi"]
   38. },
   39. "countryCode": {
   40. "policy": "include",
   41. "value": ["CN", "HK"]
   42. }
   43. }
   44. }

   46. //Ability2
   47. {
   48. "module": {
   49. "name": "module_sample2",
   50. "deviceType":  ["tv", "tablet"],
   51. "metadata": [
   52. {
   53. "name": "distributionFilter_config",
   54. "resource": "$profile:distributionFilter_config_sample2"
   55. }
   56. ],
   57. "abilities": [
   58. {
   59. "name": "ability_sample"
   60. }
   61. ]
   62. }
   63. }
   64. //Ability2所属Module的distributionFilter
   65. {
   66. "distributionFilter": {
   67. "apiVersion" : {
   68. "policy": "include",
   69. "value": [10,11]
   70. },
   71. "screenShape": {
   72. "policy": "include",
   73. "value": ["rect"]
   74. },
   75. "screenWindow": {
   76. "policy": "include",
   77. "value": ["454*454", "466*466"]
   78. },
   79. "screenDensity": {
   80. "policy": "include",
   81. "value": ["ldpi", "xldpi"]
   82. },
   83. "countryCode": {
   84. "policy": "include",
   85. "value": ["USA", "UK"]
   86. }
   87. }
   88. }
   ```

## Entry校验逻辑

校验目的：目标设备只有一个Entry类型的Module与之对应，Feature类型的Module经过deviceType及distributionFilter指明的目标设备都需要存在Entry类型的Module。

1. 校验Feature类型的Module经过deviceType及distributionFilter指明的目标设备都存在Entry类型的Module。

   例如，Bundle中存在一个Entry类型Module1，其支持设备为tablet和wearable，其分发规则为circle和rect形状的屏幕，同时存在一个Feature类型的Module2，通过分发规则可知，其可以分发到rect形状的tablet和wearable设备上，而rect形状的tablet和wearable设备上存在Entry类型的Module1，校验通过。

   ```
   1. //Entry类型Module1
   2. {
   3. "module": {
   4. "name": "module_sample1",
   5. "type": "entry",
   6. "deviceType": ["tablet", "wearable"],
   7. "metadata": [
   8. {
   9. "name": "distributionFilter_config",
   10. "resource": "$profile:distributionFilter_config1"
   11. }
   12. ]
   13. }
   14. }
   15. //Module1的distributionFilter，distributionFilter_config1.json
   16. {
   17. "screenShape":{
   18. "policy": "include",
   19. "value": ["circle", "rect"]
   20. }
   21. }
   22. //Feature类型Module2
   23. {
   24. "module": {
   25. "name": "module_sample2",
   26. "type": "feature",
   27. "deviceType": ["tablet", "wearable"],
   28. "metadata": [
   29. {
   30. "name": "distributionFilter_config",
   31. "resource": "$profile:distributionFilter_config2"
   32. }
   33. ]
   34. }
   35. }
   36. //Module2的distributionFilter，distributionFilter_config2.json
   37. {
   38. "screenShape":{
   39. "policy": "include",
   40. "value": ["rect"]
   41. }
   42. }
   ```
2. 校验目标设备只有一个Entry类型的Module与之对应。
   1. 校验Entry类型Module的deviceType。如果deviceType不相交，校验通过。如果deviceType相交，继续校验Entry类型Module的distributionFilter。

      例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType不相交，可以有效区分两个Module，校验通过。

      ```
      1. //Entry类型Module1
      2. {
      3. "module": {
      4. "name": "module_sample1",
      5. "type": "entry",
      6. "deviceType": ["tablet"]
      7. }
      8. }
      9. //Entry类型Module2
      10. {
      11. "module": {
      12. "name": "module_sample2",
      13. "type": "entry",
      14. "deviceType": ["wearable"]
      15. }
      16. }
      ```
   2. 校验Entry类型Module的distributionFilter。如果distributionFilter不相交，校验通过。如果distributionFilter相交，校验失败，打包失败。

      例如，同一个Bundle中存在两个Entry类型的Module，分别为Module1和Module2，两者的deviceType相交，但两者的distributionFilter不相交，可以有效区分两个Module，校验通过。

      ```
      1. //Entry类型Module1
      2. {
      3. "module": {
      4. "name": "module_sample1",
      5. "type": "entry",
      6. "deviceType": ["wearable"],
      7. "metadata": [
      8. {
      9. "name":"distributionFilter_config",
      10. "resource": "$profile:distributionFilter_sample1"
      11. }
      12. ]
      13. }
      14. }
      15. //Module1的distributionFilter，distributionFilter_sample1.json
      16. {
      17. "distributionFilter": {
      18. "screenShape":{
      19. "policy": "include",
      20. "value": ["rect"]
      21. }
      22. }
      23. }
      24. //Entry类型Module2
      25. {
      26. "module": {
      27. "name": "module_sample2",
      28. "type": "entry",
      29. "deviceType": ["wearable"],
      30. "metadata": [
      31. {
      32. "name":"distributionFilter_config",
      33. "resource": "$profile:distributionFilter_sample2"
      34. }
      35. ]
      36. }
      37. }
      38. //Module2的distributionFilter，distributionFilter_sample2.json
      39. {
      40. "distributionFilter": {
      41. "screenShape":{
      42. "policy": "include",
      43. "value": ["circle"]
      44. }
      45. }
      46. }
      ```
