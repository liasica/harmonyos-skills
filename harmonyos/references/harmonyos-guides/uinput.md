---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uinput
title: uinput
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 命令行工具 > uinput
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d787b905a23abd8b15db4310086725dba37206410ad98f7bcd41a08e53896d47
---

uinput 可模拟用户操作，例如鼠标、键盘、触控板等设备，适用于稳定性等压力测试。

## 环境要求

* 根据hdc命令行工具指导，完成[环境准备](hdc.md#环境准备)。
* 确保设备已成功连接，并执行hdc shell。

## uinput功能

**用法**

```
1. uinput <option> <command> <arg> ...
```

**支持能力**

| 命令简写 | 命令全写 | 含义说明 |
| --- | --- | --- |
| -M | --mouse | 注入鼠标事件。 |
| -K | --keyboard | 注入键盘事件。 |
| -S | --stylus | 注入触控笔事件。 |
| -T | --touch | 注入触摸事件。 |
| -P | --touchpad | 注入触控板事件。 |
| -? | --help | 帮助命令。 |
| enable\_key\_status | enable\_key\_status | [控制注入的修饰键状态](uinput.md#控制注入的修饰键状态)。 |

说明

命令中与坐标相关的参数，单位均为[px(屏幕物理像素单位)](../harmonyos-references/ts-pixel-units.md)。

## 帮助命令

显示uinput工具支持的命令信息。

**命令**

```
1. uinput -?
2. uinput --help
```

**使用示例**

```
1. # 显示帮助信息
2. uinput -?

4. # 执行结果
5. Usage: uinput <option> <command> <arg>...
6. The option are:
7. -K  --keyboard
8. commands for keyboard:
9. -d <key>                   --down   <key>     -press down a key
10. -u <key>                   --up     <key>     -release a key
11. -l <key> [long press time] --long_press <key> [long press time] -press and hold the key
12. -r <key> [repeat output time] --repeat output <key> [repeat output time] -press and hold the key
13. -i <time>                  --interval <time>  -the program interval for the (time) milliseconds

15. ...
```

## 鼠标事件

模拟鼠标移动、点击等。

### 鼠标移动事件

模拟鼠标移动到以指定屏幕左上角为原点的相对坐标系的位置(dx, dy)。

**命令**

```
1. uinput -M -m <dx> <dy>
2. uinput --mouse --move <dx> <dy>

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
```

**使用示例**

```
1. # 模拟鼠标移动到以指定屏幕左上角为原点的相对坐标系的位置(100, 100)。
2. uinput -M -m 100 100
```

**扩展命令**

```
1. uinput -M -m <dx1> <dy1> <dx2> <dy2> [smooth time] --trace
2. uinput --mouse --move <dx1> <dy1> <dx2> <dy2> [smooth time] --trace

4. # <dx1> <dy1>鼠标移动起点以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>鼠标移动终点以屏幕左上角为原点的相对坐标系的位置坐标。
6. # 补充选项 --trace 可以模拟鼠标移动到以指定屏幕左上角为原点的相对坐标系的位置及过程。
7. # [smooth time]移动时间，单位：ms，默认值：1000，取值范围：[1,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟鼠标从(100, 100)花费1500ms移动到(200, 200)。
2. uinput -M -m 100 100 200 200 1500 --trace
```

### 鼠标按键按下事件

模拟鼠标按下按键，建议与鼠标按键抬起事件搭配使用，确保事件闭环。buttonId：[鼠标按键](uinput.md#鼠标按键)。

**命令**

```
1. uinput -M -d <buttonId>
2. uinput --mouse --down <buttonId>
```

### 鼠标按键抬起事件

模拟鼠标抬起按键，建议与鼠标按键按下事件搭配使用，确保事件闭环。buttonId：[鼠标按键](uinput.md#鼠标按键)。

**命令**

```
1. uinput -M -u <buttonId>
2. uinput --mouse --up <buttonId>
```

**使用示例**

```
1. # 模拟按下鼠标左键并抬起。
2. uinput -M -d 0 -u 0
```

### 鼠标按键单击事件

模拟鼠标单击按键。buttonId：[鼠标按键](uinput.md#鼠标按键)。

**命令**

```
1. uinput -M -c <buttonId>
2. uinput --mouse --click <buttonId>
```

**使用示例**

```
1. # 模拟单击鼠标左键。
2. uinput -M -c 0
```

### 双击鼠标按键事件

模拟双击鼠标按键。buttonId：[鼠标按键](uinput.md#鼠标按键)。

**命令**

```
1. uinput -M -b <dx> <dy> <buttonId> [press time] [click interval time]
2. uinput --mouse --double_click <dx> <dy> <buttonId> [press time] [click interval time]

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
5. # [press time]首次按压时间，可选参数，单位：ms，默认时间为：50，取值范围：[1,300]，仅支持整数。
6. # [click interval time]点击间隔时间，可选参数，单位：ms，默认时间为：300，取值范围：[1,450]，仅支持整数。
```

**使用示例**

```
1. # 模拟在（100, 150）位置双击鼠标左键。
2. uinput -M -b 100 150 0 10 10
```

### 鼠标滚轴滚动事件

模拟鼠标滚轴向前/向后滚动，需与鼠标移动事件搭配使用。

**命令**

```
1. uinput -M -m <dx1> <dy1> -s <number>
2. uinput --mouse --move <dx1> <dy1> --scroll <number>

4. # <dx1> <dy1>以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <number>鼠标滚动刻度数，正数向后滚动，负数向前滚动，一个刻度是15，仅支持整数。
```

**使用示例**

```
1. # 模拟鼠标移动到以指定屏幕左上角为原点的相对坐标系的位置(100, 200)，鼠标滚轴向后滚动三个刻度。
2. uinput -M -m 100 200 -s 45
```

### 鼠标拖拽事件

模拟鼠标拖拽。

**命令**

```
1. uinput -M -g <dx1> <dy1> <dx2> <dy2> [total time]
2. uinput --mouse --drag <dx1> <dy1> <dx2> <dy2> [total time]

4. # <dx1> <dy1>鼠标拖拽起点以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>鼠标拖拽终点以屏幕左上角为原点的相对坐标系的位置坐标。
6. # [total time]拖拽总耗时，可选参数，单位：ms，默认值为1000，取值范围：[1,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟按下鼠标左键从(200, 650)耗时15000ms拖动到(500, 300)后释放鼠标左键。
2. uinput -M -g 200 650 500 300 15000
```

### 设置鼠标事件间隔

设置鼠标事件的程序间隔，以ms为单位。需与其它鼠标事件命令搭配使用，否则此命令无效。

**命令**

```
1. uinput -M -i <time>
2. uinput --mouse --interval <time>

4. # <time>鼠标事件间隔时间，单位：ms，取值范围：[1,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟单击鼠标左键间隔500ms后再次单击鼠标左键。
2. uinput -M -c 0 -i 500 -c 0
```

### 鼠标按键

| buttonId | 含义说明 |
| --- | --- |
| 0 | 鼠标左键 |
| 1 | 鼠标右键 |
| 2 | 鼠标中键 |
| 3 | 鼠标侧边键 |
| 4 | 鼠标扩展键 |
| 5 | 鼠标前进键 |
| 6 | 鼠标后退键 |
| 7 | 鼠标任务键 |

### 查询鼠标光标信息

查询当前鼠标光标信息。

如果鼠标光标处于显示状态，将输出鼠标光标显示状态及[鼠标光标样式](../harmonyos-references/js-apis-pointer.md#pointerstyle)。若传入filePath参数且鼠标光标为第三方自定义光标（样式枚举值为-100），会将鼠标光标样式图以二进制形式保存到指定文件中。需要自行创建filePath文件。若未传入filePath参数，将不会保存样式图。当鼠标光标处于隐藏状态时，不会输出样式信息，也不会保存样式图。

**命令**

```
1. uinput -M -q [filePath]

3. # [filePath] 鼠标光标的样式图文件保存路径，可选参数，当前版本仅支持“/data/local/tmp/”目录下的文件保存路径，例如：/data/local/tmp/testfile。
```

**使用示例**

```
1. # 查询当前鼠标光标的显示/隐藏状态和样式ID。
2. uinput -M -q

4. # 查询当前鼠标光标的显示/隐藏状态和样式ID，并将鼠标光标样式图以二进制形式写入“/data/local/tmp/testfile”文件中。
5. touch /data/local/tmp/testfile
6. uinput -M -q /data/local/tmp/testfile
```

## 键盘事件

模拟键盘按键输入。

### 键盘按键按下事件

模拟键盘按下按键，建议与键盘按键抬起事件搭配使用，确保事件闭环。keyCode：[键值定义说明](../harmonyos-references/js-apis-keycode.md)。

**命令**

```
1. uinput -K -d <keyCode>
2. uinput --keyboard --down <keyCode>
```

### 键盘按键抬起事件

模拟键盘抬起按键，必须与键盘按键按下事件搭配使用，确保事件闭环。keyCode：[键值定义说明](../harmonyos-references/js-apis-keycode.md)。

**命令**

```
1. uinput -K -u <keyCode>
2. uinput --keyboard --up <keyCode>
```

**使用示例**

```
1. # 模拟按下"A"键并抬起。
2. uinput -K -d 2017 -u 2017
```

### 键盘按键长按事件

模拟键盘按下一个按键并保持设定的时长后抬起，无需再次注入键盘按键抬起事件。长按期间不会重复注入按键按下事件。keyCode：[键值定义说明](../harmonyos-references/js-apis-keycode.md)。

**命令**

```
1. uinput -K -l <keyCode> [long press time]
2. uinput --keyboard --long_press <keyCode> [long press time]

4. # [long press time]长按时间，可选参数，单位：ms，默认值为3000，取值范围：[3000,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟按下"A"键并保持6000ms后抬起。
2. uinput -K -l 2017 6000
```

### 键盘按键持续输入事件

模拟键盘按下一个按键并在设定的时长内持续输入按下事件后抬起，无需再次注入键盘按键抬起事件。长按期间会重复注入按键按下事件。keyCode：[键值定义说明](../harmonyos-references/js-apis-keycode.md)。

**命令**

```
1. uinput -K -r <keyCode> [repeat output time]
2. uinput --keyboard --repeat <keyCode> [repeat output time]

4. # [repeat output time]重复上报按键按下事件的持续时间，可选参数，单位：ms，默认值为3000，取值范围：[3000,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟按下"A"键并在4000ms内重复输入。
2. uinput -K -r 2017 4000
```

### 设置键盘事件间隔

设置键盘事件的程序间隔，以ms为单位。需与其它键盘事件命令搭配使用，否则此命令无效。

**命令**

```
1. uinput -K -i <time>
2. uinput --keyboard --interval <time>

4. # <time>键盘事件间隔时间，单位：ms，取值范围：[1,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟按下键盘"A"键间隔500ms后释放。
2. uinput -K -d 2017 -i 500 -u 2017
```

### 键盘文本输入事件

模拟键盘输入文本。不支持与其它命令组合使用。只支持ASCII字符，最大支持输入字符2000个。

**命令**

```
1. uinput -K -t <text>
2. uinput --keyboard --text <text>
```

**使用示例**

```
1. # 模拟输入一段文本"Hello,World!"
2. uinput -K -t Hello,World!
```

## 控制注入的修饰键状态

从API version 22开始，支持启用或禁用控制注入的修饰键状态能力，支持的修饰键包括：KEYCODE\_ALT\_LEFT、KEYCODE\_ALT\_RIGHT、KEYCODE\_SHIFT\_LEFT、KEYCODE\_SHIFT\_RIGHT、KEYCODE\_CTRL\_LEFT、KEYCODE\_CTRL\_RIGHT、KEYCODE\_META\_LEFT、KEYCODE\_META\_RIGHT，具体请参考keyCode：[键值定义说明](../harmonyos-references/js-apis-keycode.md)。

### 启用控制注入的修饰键状态能力

启用控制注入的修饰键状态能力并设置维持时间。需要与uinput键盘按键按下事件配合使用，启用后再注入指定修饰键的按下事件，可维持指定时间的按下状态，维持时间结束后自动触发该修饰键抬起事件。

**命令**

```
1. uinput enable_key_status <enable> [duration]

3. # <enable> 控制注入的修饰键状态能力，取值为1或0，取值为1表示启用控制注入的修饰键状态能力，0表示禁用控制注入的修饰键状态能力。
4. # [duration] 控制注入的修饰键状态持续时间，可选参数，单位：s，默认值为10，取值范围：[1,10]，仅支持整数。
```

**使用示例**

```
1. # 启用控制注入的修饰键状态能力，未设置修饰键状态维持时间。注入KEYCODE_SHIFT_LEFT按键（取值为2047）按下事件，可维持10s按下状态。
2. uinput enable_key_status 1
3. uinput -K -d 2047

5. # 启用控制注入的修饰键状态能力并设置修饰键状态维持时间为5s。注入KEYCODE_SHIFT_LEFT按键（取值为2047）按下事件，可维持5s按下状态。
6. uinput enable_key_status 1 5
7. uinput -K -d 2047
```

### 禁用控制注入的修饰键状态能力

禁用控制注入的修饰键状态能力，直到下次启用恢复该能力。

**命令**

```
1. # <enable> 控制注入的修饰键状态能力，取值为1或0，取值为1表示启用控制注入的修饰键状态能力，0表示禁用控制注入的修饰键状态能力。
2. uinput enable_key_status <enable>
```

**使用示例**

```
1. # 禁用控制注入的修饰键状态能力。
2. uinput enable_key_status 0
```

## 触控笔事件

模拟触控笔点击、滑动等。实际注入效果与[触摸事件](uinput.md#触摸事件)一致，建议优先使用触摸事件命令。

### 触控笔按下事件

模拟触控笔在（dx dy）按下，建议与触控笔抬起事件搭配使用，确保事件闭环。

**命令**

```
1. uinput -S -d <dx> <dy>
2. uinput --stylus --down <dx> <dy>

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
```

### 触控笔抬起事件

模拟触控笔在（dx dy）抬起，建议与触控笔按下事件搭配使用，确保事件闭环。

**命令**

```
1. uinput -S -u <dx> <dy>
2. uinput --stylus --up <dx> <dy>

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
```

**使用示例**

```
1. # 模拟在（100, 100）位置按下并抬起。
2. uinput -S -d 100 100 -u 100 100
```

### 触控笔移动事件

模拟触控笔从（dx1, dy1）按下在指定时间内移动到（dx2, dy2）后抬起。

**命令**

```
1. uinput -S -m <dx1> <dy1> <dx2> <dy2> [smooth time] [-k keep time]
2. uinput --stylus --move <dx1> <dy1> <dx2> <dy2> [smooth time] [-k keep time]

4. # <dx1> <dy1>触控笔移动起点以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>触控笔移动终点以屏幕左上角为原点的相对坐标系的位置坐标。
6. # [smooth time]移动时间，可选参数，单位：ms，默认值为1000，取值范围：[1,15000]，仅支持整数。
7. # [-k keep time]移动至目标位置后抬起前的停留时间，可选参数，单位：ms，默认值为0，取值范围：[0,60000]，仅支持整数。
```

**使用示例**

```
1. # 模拟触控笔从(100, 1000)按下，花费1000ms移动到(100, 2000)后，保持按下1000ms后抬起。
2. uinput -S -m 100 1000 100 2000 1000 -k 1000
```

### 触控笔单击事件

模拟触控笔在(dx, dy)位置单击。

**命令**

```
1. uinput -S -c <dx> <dy> [click interval]
2. uinput --stylus --click <dx> <dy> [click interval]

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
5. # [click interval]点击间隔时间，可选参数，单位：ms，默认值为100，取值范围：[1,450]，仅支持整数。
```

**使用示例**

```
1. # 模拟触控笔在(100, 100)位置单击。
2. uinput -S -c 100 100
```

### 触控笔拖拽事件

模拟触控笔拖拽。

**命令**

```
1. uinput -S -g <dx1> <dy1> <dx2> <dy2> [press time] [total time]
2. uinput --stylus --drag <dx1> <dy1> <dx2> <dy2> [press time] [total time]

4. # <dx1> <dy1>触控笔拖拽起点以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>触控笔拖拽终点以屏幕左上角为原点的相对坐标系的位置坐标。
6. # [press time]按压时间，可选参数，需要与total time配合使用，如果有任一缺省，则命令不生效。同时缺省，命令生效。单位：ms，默认值为500，取值范围：[500,14500]，仅支持整数。
7. # [total time]拖动时间，可选参数，需要与press time配合使用，如果有任一缺省，则命令不生效。同时缺省，命令生效。单位：ms，默认值为1000，取值范围：[1000,15000]，仅支持整数。[total time] - [press time]不能少于500，否则命令报错：total time input is error。
```

**使用示例**

```
1. # 模拟触控笔从(100, 150)长按500ms后开始拖拽并在1100ms后拖动到(500, 300)释放。
2. uinput -S -g 100 150 500 300 500 1100
```

### 设置触控笔事件间隔

设置触控笔事件的程序间隔，以ms为单位。需与其它触控笔事件命令搭配使用，否则此命令无效。

**命令**

```
1. uinput -S -i <time>
2. uinput --stylus --interval <time>

4. # <time>间隔时间，单位：ms，取值范围：[1,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟触控笔在(100, 100)位置按下后，间隔500ms后在(100, 100)位置抬起。
2. uinput -S -d 100 100 -i 500 -u 100 100
```

## 触摸事件

模拟手指触摸点击、滑动等。

### 触摸按下事件

模拟手指触摸在（dx dy）按下，建议与触摸抬起事件搭配使用，确保事件闭环。

**命令**

```
1. uinput -T -d <dx> <dy>
2. uinput --touch --down <dx> <dy>

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
```

### 触摸抬起事件

模拟手指触摸在（dx dy）抬起，建议与触摸按下事件搭配使用，确保事件闭环。

**命令**

```
1. uinput -T -u <dx> <dy>
2. uinput --touch --up <dx> <dy>

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
```

**使用示例**

```
1. # 模拟手指触摸在（100, 100）位置按下并抬起。
2. uinput -T -d 100 100 -u 100 100
```

### 触摸移动事件

模拟手指触摸从(dx1, dy1)按下在指定时间内移动到(dx2, dy2)后抬起，最多支持三指同时移动。

**命令**

```
1. uinput -T -m <dx1> <dy1> <dx2> <dy2> [-k keep time] [smooth time]
2. uinput --touch --move <dx1> <dy1> <dx2> <dy2> [-k keep time] [smooth time]

4. # <dx1> <dy1>触摸移动起点以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>触摸移动终点以屏幕左上角为原点的相对坐标系的位置坐标。
6. # [-k keep time]按下保持时间，可选参数，单位：ms，默认值为0，取值范围：[0,60000]，仅支持整数。
7. # [smooth time]移动时间，可选参数，单位：ms，默认值为1000，取值范围：[1,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟手指触摸从(100, 1000)按下，花费1000ms移动到(100, 2000)后，保持按下1000ms后抬起。
2. uinput -T -m 100 1000 100 2000 -k 1000 1000

4. # 模拟三指滑动，第一根手指触摸按下从（300, 900）移动到（300, 2000），第二根手指触摸按下从（600, 900）移动到（600, 2000），第三根手指触摸按下从（900, 900）移动到（900, 2000），移动总时长为200ms，移动结束后手指在屏幕停顿1000m后再抬起。
5. uinput -T -m 300 900 300 2000 600 900 600 2000 900 900 900 2000 -k 1000 200
```

### 触摸单击事件

模拟手指触摸在(dx, dy)位置单击。

**命令**

```
1. uinput -T -c <dx> <dy> [click interval]
2. uinput --touch --click <dx> <dy> [click interval]

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
5. # [click interval]点击间隔时间，可选参数，单位：ms，默认值为100，取值范围：[1,450]，仅支持整数。
```

**使用示例**

```
1. # 模拟手指触摸在(100, 100)位置单击。
2. uinput -T -c 100 100
```

### 触摸拖拽事件

模拟手指触摸拖拽。

**命令**

```
1. uinput -T -g <dx1> <dy1> <dx2> <dy2> [press time] [total time]
2. uinput --touch --drag <dx1> <dy1> <dx2> <dy2> [press time] [total time]

4. # <dx1> <dy1>触摸拖拽起点以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>触摸拖拽终点以屏幕左上角为原点的相对坐标系的位置坐标。
6. # [press time]按压时间，可选参数，需要与total time配合使用，如果有任一缺省，则命令不生效。同时缺省，命令生效。单位：ms，默认值为500，取值范围：[500,14500]，仅支持整数。
7. # [total time]拖动时间，可选参数，需要与press time配合使用，如果有任一缺省，则命令不生效。同时缺省，命令生效。单位：ms，默认值为1000，取值范围：[1000,15000]，仅支持整数。[total time] - [press time]不能少于500，否则命令报错：total time input is error。
```

**使用示例**

```
1. # 模拟手指按下从(100, 150)在1100ms拖动到(500, 300)后释放。
2. uinput -T -g 100 150 500 300 500 1100
```

### 设置触摸事件间隔

设置触摸事件的程序间隔，以ms为单位。需与其它触摸事件命令搭配使用，否则此命令无效。

**命令**

```
1. uinput -T -i <time>
2. uinput --touch --interval <time>

4. # <time>间隔时间，单位：ms，取值范围：[1,15000]，仅支持整数。
```

**使用示例**

```
1. # 模拟手指在(100, 100)位置按下后，间隔500ms后在(100, 100)位置抬起。
2. uinput -T -d 100 100 -i 500 -u 100 100
```

### 触摸屏单指关节双击事件

模拟触摸屏单指关节双击。

**命令**

```
1. uinput -T -k -s <dx1> <dy1> <dx2> <dy2> [interval time]
2. uinput --touch --knuckle --single <dx1> <dy1> <dx2> <dy2> [interval time]

4. # <dx1> <dy1>单指关节第一次敲击以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>单指关节第二次敲击以屏幕左上角为原点的相对坐标系的位置坐标。
6. # [interval time]间隔时间，可选参数，单位：ms，默认值200，取值范围：[1,250]，仅支持整数。
```

**使用示例**

```
1. # 模拟单指关节在(100, 100)、(100, 130)位置间隔200ms敲击。
2. uinput -T -k -s 100 100 100 130
```

### 触摸屏双指关节双击事件

模拟触摸屏双指关节双击。

**命令**

```
1. uinput -T -k -d <dx1> <dy1> <dx2> <dy2> [interval time]
2. uinput --touch --knuckle --double <dx1> <dy1> <dx2> <dy2> [interval time]

4. # <dx1> <dy1>第一个指关节以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <dx2> <dy2>第二个指关节以屏幕左上角为原点的相对坐标系的位置坐标。
6. # [interval time]间隔时间，可选参数，单位：ms，默认值200，取值范围：[1,250]，仅支持整数。
```

**使用示例**

```
1. # 模拟双指关节分别在(100, 100)、(100, 130)位置间隔200ms敲击2次。
2. uinput -T -k -d 100 100 100 130
```

## 触控板事件

### 触控板捏合事件

模拟触控板手指捏合。

**命令**

```
1. uinput -P -p <dx> <dy> scalePercent
2. uinput --touchpad --pinch <dx> <dy> scalePercent

4. # <dx> <dy>以屏幕左上角为原点的相对坐标系的位置坐标。
5. # scalePercent收缩百分比，取值范围：[1,500]。小于100是缩小，大于100是放大。设置时要求dx大于0，dy大于等于200。此场景只支持图片缩放，调用该命令时，确保桌面上有一张图片。
```

**使用示例**

```
1. # 模拟触控板手指捏合。
2. uinput -P -p 100 300 89
```

### 触控板滑动事件

模拟触控板滑动。

**命令**

```
1. uinput -P -s <startX> <startY> <endX> <endY>
2. uinput --touchpad --swipe <startX> <startY> <endX> <endY>

4. # <startX> <startY>触控板上报滑动手势事件的起点以屏幕左上角为原点的相对坐标系的位置坐标。
5. # <endX> <endY>触控板上报滑动手势事件的终点以屏幕左上角为原点的相对坐标系的位置坐标。
```

**使用示例**

```
1. # 模拟触控板三指滑动手势。
2. uinput -P -s 100 1100 100 300
```

### 触控板旋转事件

模拟触控板旋转。

当前触摸板旋转事件执行无效果。

**命令**

```
1. uinput -P -r <rotateValue>
2. uinput --touchpad --rotate <rotateValue>

4. # <rotateValue>旋转值，单位：度（°），取值范围：[-359,359]，仅支持整数。旋转角度为正值时，顺时针旋转，旋转角度为负值时，逆时针旋转。
```

**使用示例**

```
1. # 模拟触控板双指旋转180°。
2. uinput -P -r 180
```
