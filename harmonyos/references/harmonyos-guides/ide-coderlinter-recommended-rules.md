---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-coderlinter-recommended-rules
title: recommended推荐规则清单
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > recommended推荐规则清单
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e71be2c6e5c637064a4011b39f334e8e20d80a7aadbbda03e7b652f67d594a6d
---

## 通用规则推荐规则集@typescript-eslint/recommended

|  |  |
| --- | --- |
| @typescript-eslint/await-thenable | 不允许对不是“Thenable”对象的值使用await关键字（“Thenable”表示某个对象拥有“then”方法，比如Promise）。 |
| @typescript-eslint/consistent-type-imports | 强制使用一致的类型导入风格。 |
| @typescript-eslint/explicit-function-return-type | 函数和类方法需要显式的定义返回类型。 |
| @typescript-eslint/explicit-module-boundary-types | 导出到外部的函数和公共类方法，需要显式的定义返回类型和参数类型。 |
| @typescript-eslint/no-dynamic-delete | 不允许在computed key表达式上使用“delete”运算符。 |
| @typescript-eslint/no-explicit-any | 不允许使用“any”类型。 |
| @typescript-eslint/no-for-in-array | 禁止使用 for-in 循环来遍历数组元素。 |
| @typescript-eslint/no-this-alias | 禁止将“this”赋值给一个变量。 |
| @typescript-eslint/no-unnecessary-type-constraint | 不允许在泛型中使用不必要的约束条件。 |
| @typescript-eslint/no-unsafe-argument | 不允许将any类型的值作为函数的参数传入。 |
| @typescript-eslint/no-unsafe-assignment | 禁止将“any”类型的值赋值给变量和属性。 |
| @typescript-eslint/no-unsafe-call | 禁止调用“any”类型的表达式。 |
| @typescript-eslint/no-unsafe-member-access | 禁止成员访问“any”类型的值。 |
| @typescript-eslint/no-unsafe-return | 函数禁止返回类型为“any”的值。 |
| @typescript-eslint/prefer-literal-enum-member | 要求所有枚举成员都定义为字面量值。 |

## 安全规则推荐规则集@security/recommended

|  |  |
| --- | --- |
| @security/no-commented-code | 不使用的代码段建议直接删除，不允许通过注释的方式保留。 |
| @security/no-unsafe-aes | 该规则禁止在AES加密算法中使用不安全的ECB加密模式。 |
| @security/no-unsafe-dh | 该规则禁止使用不安全的DH密钥协商算法。 |
| @security/no-unsafe-dh-key | 该规则禁止使用不安全的DH密钥。 |
| @security/no-unsafe-dsa | 该规则禁止使用不安全的DSA签名算法。 |
| @security/no-unsafe-dsa-key | 该规则禁止使用不安全的DSA密钥。 |
| @security/no-unsafe-ecdsa | 该规则禁止在ECDSA签名算法中使用不安全的SHA1摘要算法。 |
| @security/no-unsafe-hash | 该规则使用禁止不安全的哈希算法。 |
| @security/no-unsafe-mac | 该规则禁止在MAC消息认证算法中使用不安全的哈希算法。 |
| @security/no-unsafe-rsa-encrypt | 该规则禁止使用不安全的RSA非对称加密算法。 |
| @security/no-unsafe-rsa-key | 该规则禁止使用不安全的RSA密钥。 |
| @security/no-unsafe-rsa-sign | 该规则禁止不安全的RSA签名算法。 |
| @security/no-unsafe-3des | 该规则禁止使用不安全的3DES加密模式。 |

## 性能规则推荐规则集@performance/recommended

|  |  |
| --- | --- |
| @performance/foreach-args-check | 建议在ForEach参数中设置keyGenerator。 |
| @performance/high-frequency-log-check | 不建议在高频函数中使用Hilog。 |
| @performance/hp-arkts-no-use-any-export-current | 避免使用export \* 导出当前module中定义的类型和数据。 |
| @performance/hp-arkts-no-use-any-export-other | 避免使用export \* 导出其他module中定义的类型和数据。 |
| @performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse | 避免在aboutToReuse中对自动更新值的状态变量进行更新。 |
| @performance/hp-arkui-combine-same-arg-animateto | 建议动画参数相同时使用同一个animateTo。 |
| @performance/hp-arkui-load-on-demand | 建议使用按需加载。 |
| @performance/hp-arkui-no-func-as-arg-for-reusable-component | 避免使用函数作为复用的自定义组件创建时的入参。 |
| @performance/hp-arkui-no-state-var-access-in-loop | 避免在for、while等循环逻辑中频繁读取状态变量。 |
| @performance/hp-arkui-no-stringify-in-lazyforeach-key-generator | 在使用LazyForEach进行组件复用的key生成器函数里，不要使用stringify。 |
| @performance/hp-arkui-replace-nested-reusable-component-by-builder | 建议使用@Builder替代嵌套的自定义组件。 |
| @performance/hp-arkui-set-cache-count-for-lazyforeach-grid | 建议在Grid下使用LazyForEach时设置合理的cacheCount。 |
| @performance/hp-arkui-suggest-cache-avplayer | 建议缓存AVPlayer实例减少起播时延。 |
| @performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component | 建议使用reuseId标记不同结构的组件构成。 |
| @performance/hp-arkui-suggest-use-effectkit-blur | 建议使用effectKit.createEffect实现模糊效果。 |
| @performance/hp-arkui-use-grid-layout-options | 建议在指定位置时使用GridLayoutOptions提升Grid性能。 |
| @performance/hp-arkui-use-local-var-to-replace-state-var | 建议使用临时变量替换状态变量。 |
| @performance/hp-arkui-use-object-link-to-replace-prop | 建议使用@ObjectLink代替@Prop减少不必要的深拷贝。 |
| @performance/hp-arkui-use-onAnimationStart-for-swiper-preload | 建议Swiper预加载机制搭配 OnAnimationStart 接口回调使用。 |
| @performance/hp-arkui-use-reusable-component | 建议复杂组件的定义，尽量使用组件复用。 |
| @performance/hp-arkui-use-scale-to-replace-attr-animateto | 建议组件布局改动时使用图形变换属性动画。 |
| @performance/hp-arkui-use-transition-to-replace-animateto | 建议组件转场动画使用transition。 |
| @performance/hp-ffrt-no-use-std | 禁止在FFRT worker中使用std::xxx等同步接口。 |
| @performance/no-high-loaded-frame-rate-range | 不允许锁定最高帧率运行。 |
| @performance/start-window-icon-check | 启动页图标分辨率建议不超过256 \* 256。 |
| @performance/waterflow-data-preload-check | 建议对waterflow子组件进行数据预加载。 |
| @performance/web-on-active-check | 使用了Web预渲染技术的应用，建议在预渲染完成后（onFirstMeaningfulPaint），调用停止渲染接口（onInactive）。 |
| @performance/gif-hardware-decoding-check | 在使用@ohos/gif-drawable库解码gif图片时，建议开启硬解码，提升gif加载性能。 |
| @performance/no-use-any-import | 使用import的方式引入对应的模块时，建议按需引用使用到的变量代替“import \*”的方式，以减少 .ets文件的执行耗时和文件中所有export变量的初始化过程。 |
| @performance/avoid-overusing-custom-component-check | 当在应用中使用自定义组件时，可以优先使用@Builder函数代替自定义组件，@Builder函数不会在后端FrameNode节点树上创建一个新的树节点，有助于缩短页面的加载和渲染时长。 |
| @performance/bad-deep-clone-check | 避免使用不合理深拷贝，如JSON.parse(JSON.stringify(foo))和\_.cloneDeep(foo)。 |
| @performance/reuse-date-instances-check | 用于检测在循环或调用频繁的方法中重复创建Date对象，建议开发者重用现有实例或使用时间戳进行计算，减少创建Date成本。 |
| @performance/crypto-replacement-check | 对于三方库@ohos/crypto-js所提供的大部分接口，SDK（@ohos.security.cryptoFramework）中有对应的系统原生实现。建议使用系统原生接口。 |
| @performance/monitor-invisible-area-in-image-animation | 使用ImageAnimation实现帧动画时，建议显式调用monitorInvisibleArea接口。在动画组件不可见时，会停止动画播放，减少无效的冗余动画带来的负载恶化。 |
| @performance/datashare-query-unrelease-check | 建议使用DataShareHelper的query接口查询数据得到结果后，应及时关闭，避免造成内存泄露。 |
| @performance/update-state-var-between-animatetos-check | 如果多个animateTo之间存在状态更新，会导致执行下一个animateTo之前又存在需要更新的脏节点，可能造成冗余更新。因此不建议在两次animateTo之间进行状态变量更新。 |

## 预览规则集@previewer/recommended

|  |  |
| --- | --- |
| @previewer/mandatory-default-value-for-local-initialization | 如果组件的属性支持本地初始化，需要设置一个合法的不依赖运行时的默认值。 |
| @previewer/no-page-method-on-preview-component | 禁止在非路由组件上实例化onPageShow、onPageHide、onBackPress等页面级方法。 |
| @previewer/no-unallowed-decorator-on-root-component | 对于@Entry组件，不允许使用@Consume、@Link、@ObjectLink、@Prop注解；对于@Preview组件，建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件作为预览该组件的容器。 |

## 一次开发多端部署规则推荐规则集@cross-device-app-dev/recommended

|  |  |
| --- | --- |
| @cross-device-app-dev/color-contrast | 文本和背景之间的颜色对比度至少为4.5:1以确保可读性。 |
| @cross-device-app-dev/color-value | 颜色值应当使用“$r”从color.json中引用，以适配不同的系统颜色模式，禁止使用固定的值。 |
| @cross-device-app-dev/font-size | 字体大小要求至少为8fp以便于阅读。 |
| @cross-device-app-dev/font-size-unit | 字体大小单位建议使用fp，以适配系统字体设置。 |
| @cross-device-app-dev/grid-columns-span | 不推荐开发者将栅格中所有的GridCol子组件只设置span属性，且值与父组件的columns属性相等。 |
| @cross-device-app-dev/grid-span-value | 在栅格布局组件GridCol中，span和offset不建议使用小数。 |
| @cross-device-app-dev/sidebar-navigation | 对于2in1和tablet设备，应将Tabs组件设置为侧边导航栏。 |
| @cross-device-app-dev/size-unit | 组件通用属性width、height和size，应当使用vp作为单位，以适配不同设备屏幕宽度。 |
| @cross-device-app-dev/touch-target-size | 组件通用属性responseRegion点击热区需满足最小尺寸要求。 |
| @cross-device-app-dev/one-multi-breakpoint-check | 一多特性必须使用系统断点判断是否开启，不能通过设备类型、设备方向或是否可折叠等属性来判断。 |

## ArkTS代码风格规则推荐规则集@hw-stylistic/recommended

|  |  |
| --- | --- |
| @hw-stylistic/array-bracket-spacing | 强制数组“[”之后和“]”之前加空格。该规则仅检查.ets文件类型。 |
| @hw-stylistic/brace-style | 强制大括号和语句位于同一行。该规则仅检查.ets文件类型。 |
| @hw-stylistic/comma-spacing | 强制数组元素和函数中多个参数之间的逗号后面加空格，逗号前不加空格。该规则仅检查.ets文件类型。 |
| @hw-stylistic/curly | 条件语句和循环语句的逻辑代码必须写在大括号中。该规则仅检查.ets文件类型。 |
| @hw-stylistic/file-naming-convention | 强制代码文件和资源文件保持一致的命名风格。 |
| @hw-stylistic/indent | 强制switch语句中的case和default缩进一层。该规则仅检查.ets文件类型。 |
| @hw-stylistic/keyword-spacing | 在关键字前后强制加空格。该规则仅检查.ets文件类型。 |
| @hw-stylistic/max-len | 强制代码行最大长度为120个字符。该规则仅检查.ets文件类型。 |
| @hw-stylistic/no-multi-spaces | 不允许出现连续多个空格，除非是换行。该规则仅检查.ets文件类型。 |
| @hw-stylistic/no-tabs | 禁止使用tab作为缩进，推荐使用空格。该规则仅检查.ets文件类型。 |
| @hw-stylistic/object-property-newline | 强制对象属性换行。 |
| @hw-stylistic/one-var-declaration-per-line | 变量声明时，要求一次仅声明一个变量。该规则仅检查.ets文件类型。 |
| @hw-stylistic/operator-linebreak | 强制运算符位于代码行末。 |
| @hw-stylistic/quotes | 强制字符串使用单引号。 |
| @hw-stylistic/semi-spacing | 强制分号之前不加空格。 |
| @hw-stylistic/space-before-blocks | 强制在“{”之前加空格。 |
| @hw-stylistic/space-before-function-paren | 在函数名和“(”之间强制不加空格。该规则仅检查.ets文件类型。 |
| @hw-stylistic/space-infix-ops | 强制运算符前后都加空格。 |
