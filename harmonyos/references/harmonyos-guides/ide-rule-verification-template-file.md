---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-rule-verification-template-file
title: 模板文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 自定义元数据规则校验插件 > 模板文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c3c3e266afc15ca469f5692936496f2c23c015fce2335bc22645c3e16052f4ce
---

模板文件中包含自定义元数据规则校验插件需要的三个文件：自定义规则校验函数模板文件checkField.ts，自定义规则校验配置模板文件CustomExtensionValidationConfig.json和ts编译为js的配置模板文件tsconfig.json。

请创建指定名称的文件，并把下方源码拷贝到文件中。

## 自定义规则校验函数模板文件checkField.ts

```screen
//如果自定义校验规则文件checkField.ts存储在默认位置（ohpm-repo解压根目录的plugins/fieldCheckPlugin文件夹内），插件文件checkField.ts中默认工具类引用地址如下
import {
  FieldDataType,
  ValidationExtensionRule
} from '../../libs/service/validator/validationExtensionRule/ValidationExtensionRule';      
import {UserBasicInfo} from '../../libs/service/validator/validationExtensionRule/type';
import {CustomValidateError} from '../../libs/service/validator/CustomValidateError';
import {OhpmLazyLogger as log} from '../../libs/packages/log';
/**
 * 自定义规则校验
 * @param fieldData 字段的取值
 * @param userInfo 发布三方包用户的信息，包含userName和userRole两部分
 *    userInfo.userName：发布三方包账户的用户名称
 *    userInfo.userRole：发布三方包账户的用户角色，1表示为管理员账户，0表示为普通用户
 */
export const checkField: ValidationExtensionRule = (fieldData: FieldDataType, userInfo: UserBasicInfo): void => {
  const name: string = <string>fieldData;      // 待校验字段的值，以name为例
  const userName: string = userInfo.userName;  // 发布三方包账户的用户名称
  const userRole: number = userInfo.userRole;  // 发布三方包账户的用户角色，1表示为管理员账户，0表示为普通用户
  // 错误抛出分为两部分：CustomValidateError第一个参数内容将打印在ohpm-repo运行日志中（命令行和ohpm-repo管理界面发布三方包均会打印），第二个参数内容将打印在ohpm-repo管理界面弹窗（仅限ohpm-repo管理界面发布三方包）
  if (name === 'package') {
    throw new CustomValidateError('Cannot publish package named "package"',
      '不能发布包名为package的包');
  }
  // 成功日志打印，日志级别打印可以为：log.trace，log.debug，log.info，log.warn和log.error
  log.info('校验成功');  // log.debug('校验成功');
 };
```

## 自定义规则校验配置模板文件CustomExtensionValidationConfig.json

```screen
[
  {
    "attrName": "<被校验字段的名称1>",
    "configs": [
      {
        "ruleType": "规则的类型，不配置默认为CustomFunction",
        "description": "<规则的功能描述>",
        "ruleContent": "<规则的内容>"
      },
      {
        "ruleType": "规则的类型，不配置默认为CustomFunction",
        "description": "<规则的功能描述>",
        "ruleContent": "<规则的内容>"
      }
    ]
  },
  {
    "attrName": "<被校验字段的名称2>",
    "configs": [
      {
        "ruleType": "规则的类型，不配置默认为CustomFunction",
        "description": "<规则的功能描述>",
        "ruleContent": "<规则的内容>"
      },
      {
        "ruleType": "规则的类型，不配置默认为CustomFunction",
        "description": "<规则的功能描述>",
        "ruleContent": "<规则的内容>"
      }
    ]
  }
]
```

## ts编译为js的配置模板文件tsconfig.json

```screen
// tsconfig.json 文件指定了编译项目所需的根目录下的文件以及编译选项，编译自定义插件文件 .ts 为 .js文件。
{
  "include": [
    "plugins/fieldCheckPlugin/*" // 插件文件的位置
  ],
  "compilerOptions": {
    "target": "es2016",
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "module": "commonjs",
    "rootDirs": [
      "./src",
      "./test"
    ],
    "typeRoots": [
      "./node_modules/@types"
    ],
    "types": [
      "node",
    ],
    "resolveJsonModule": true,
    "outDir": "./plugins/outDir",   // 编译后文件输出的位置
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "alwaysStrict": true,
    "noImplicitReturns": true,
    "skipLibCheck": true
  }
}
```
