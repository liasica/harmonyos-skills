---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-aipp-configuration-file
title: 模型转换AIPP配置文件说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > AIPP > 模型转换AIPP配置文件说明
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:04+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:b95779f399d28834b45d21f55ccf9037cc3756cca54fb3353b323d08617a72d1
---

## 模型转换AIPP配置文件说明

一份功能完整的AIPP配置文件示例如下：

```proto
# AIPP的配置以aipp_op开始，标识这是一个AIPP算子的配置，aipp_op支持配置多个
aipp_op {
    # input_name参数为可选，标识对模型的哪个输入做AIPP处理
    # 类型：string
    input_name: "data"

    # related_input_rank参数为可选，与input_name对应，推荐使用input_name，当模型输入名称未知时，可使用related_input_rank标识对模型的第几个输入做AIPP处理
    # 类型：uint32
    related_input_rank: 0

    # node_after_aipp参数为可选，用于当一个输入之后有多个分支，需要对分支进行不同的AIPP处理的场景，且需满足均配置或者均不配置，不能只配置一部分分支
    # 类型：string
    node_after_aipp: "op_name"

    # input_edge_idx参数为可选，与node_after_aipp对应，当输入Data算子之后的若干算子名称重复时，可以使用input_edge_idx标识对第几个分支进行AIPP处理
    # 类型：uint32
    input_edge_idx: 0

    input_para {
        # 输入图片的类型
        # 类型：enum
        # 取值范围：[YUV420SP_U8, XRGB8888_U8, ARGB8888_U8, YUYV_U8, YUV422SP_U8, AYUV444_U8, YUV400_U8, RGB888_U8]
        format: AYUV444_U8

        shape {
            # 输入图片的宽度、高度
            # 类型：uint32
            # 取值范围 & 约束：[0,4096]、对于除了YUV400之外的YUV类型的图片，要求取值是偶数
            src_image_size_w: 800
            src_image_size_h: 600
        }

        # max_src_image_size用于动态AIPP的场景，当图片的长宽或者输入类型不确定时，设置输入图片最大的size
        # 类型：uint32
        max_src_image_size: 102400
    }

    # == Crop参数设置 == #
    crop_func {
        switch: true
        dynamic: true
        load_start_pos_w: 50
        load_start_pos_h: 50
        crop_size_w: 400
        crop_size_h: 400
    }

    # == Channel Swap参数设置 == #
    swap_func {
        dynamic: true
        rbuv_swap_switch: true
        ax_swap_switch: true
    }

    # == Resize参数设置 == #
    resize_func {
        switch: true
        dynamic: true
        resize_output_w: 200
        resize_output_h: 200
    }

    # == Color Space Conversion参数设置 == #
    csc_func {
        switch: true
        dynamic: true
        matrix_r0c0: 256
        matrix_r0c1: 0
        matrix_r0c2: 259
        matrix_r1c0: 256
        matrix_r1c1: -88
        matrix_r1c2: -183
        matrix_r2c0: 256
        matrix_r2c1: 454
        matrix_r2c2: 0
        output_bias_0: 0
        output_bias_1: 0
        output_bias_2: 0
        input_bias_0: 16
        input_bias_1: 128
        input_bias_2: 128
    }

    # == Data Type Conversion参数设置 == #
    dtc_func {
        switch: true
        dynamic: true
        mean_chn_0: 0
        mean_chn_1: 0
        mean_chn_2: 0
        mean_chn_3: 0
        min_chn_0: 0
        min_chn_1: 0
        min_chn_2: 0
        min_chn_3: 0
        var_reci_chn_0: 1.0
        var_reci_chn_1: 1.0
        var_reci_chn_2: 1.0
        var_reci_chn_3: 1.0
    }

    # == Rotation参数设置 == #
    rotation_func {
        switch: true
        dynamic: true
        rotation_angle: 0.0
    }

    # == Padding参数设置 == #
    padding_func {
        switch: true
        dynamic: true
        left_padding_size: 12
        right_padding_size: 12
        top_padding_size: 12
        bottom_padding_size: 12
        padding_value_chn_0: 20.0
        padding_value_chn_1: 20.0
        padding_value_chn_2: 20.0
        padding_value_chn_3: 20.0
    }
}
```

### AIPP配置多输入支持

AIPP支持对一个多输入模型的多个输入分别配置AIPP，也支持在一个输入Data算子有多个输出分支的情况下，对不同的输出分支分别配置AIPP。

AIPP配置的多输入支持由2组共4个配置参数控制：input\_name和related\_input\_rank用于指定对哪一个输入进行AIPP处理，node\_after\_aipp和input\_edge\_idx用于指定对Data算子的多个输出中的哪一个输出进行AIPP处理。

input\_name和related\_input\_rank两个参数推荐使用input\_name，related\_input\_rank参数用于模型输入名称不确定的场景，如果同时配置这两个参数，则两个参数互为校验；如果两个参数都没有被配置，默认对模型的第一个输入进行AIPP处理。

node\_after\_aipp和input\_edge\_idx两个参数推荐使用node\_after\_aipp，input\_edge\_idx用于Data算子的多个输出分支衔接的算子名称重复或不确定的场景，如果同时配置这两个参数，则两个参数互为校验；如果两个参数都没有被配置，则该Data算子的所有输出分支使用同一个AIPP处理。

### AIPP配置区分动态AIPP与静态AIPP

只要有一个AIPP子功能的dynamic开关配置为true，或者没有打开任何一个子功能的开关，则生成的DaVinci模型为动态AIPP模型，需要在模型推理阶段传入AIPP配置参数；相反没有任何子功能的dynamic开关配置为true，并且至少有一个子功能的开关是打开的，则生成的DaVinci模型为静态AIPP模型，模型推理阶段使用配置文件中定义的AIPP配置参数。

对于动态AIPP的场景，AIPP可以允许输入图片的长宽，以及图片类型不确定，对应即src\_image\_size\_w、src\_image\_size\_h和input\_format三个参数不配置，此时开发者需要指定动态AIPP处理时的最大图片尺寸，配置max\_src\_image\_size。

## 图片裁剪(Crop)

图片裁剪功能是指在原始图片中从指定的起点裁剪出指定大小的子图。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

* 静态配置时，crop\_size\_w和crop\_size\_h以设定的值作为输出shape。
* 动态配置时，crop\_size\_w和crop\_size\_h为预分配的最大输出shape，实际运行时设置的参数值不超过预分配的最大值。

### 静态配置

```proto
crop_func {
    switch: true
    load_start_pos_w: 50
    load_start_pos_h: 50
    crop_size_w: 150
    crop_size_h: 150
}
```

### 动态配置

```proto
crop_func {
    switch: true
    dynamic: true
    load_start_pos_w: 0
    load_start_pos_h: 0
    crop_size_w: 150
    crop_size_h: 150
}
```

## 通道交换功能(axSwap/uvSwap/rbSwap)

交换图片的通道支持AX通道交换、UV通道交换、RB通道交换。

* AX通道交换：仅支持ARGB8888、XRGB8888、AYUV444格式，其他格式不支持。
* UV通道交换：仅支持YUV420SP、YUV422SP\_U8、YUYV、AYUV444格式，其他格式不支持。
* RB通道交换：仅支持ARGB8888、XRGB8888、RGB888\_U8格式，其他格式不支持。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```proto
swap_func {
    ax_swap_switch: true
    rbuv_swap_switch: false
}
```

### 动态配置

可以不写具体的参数，在动态创建input tensor时指定。

```proto
swap_func {
    dynamic: true
    ax_swap_switch: true
    rbuv_swap_switch: false
}
```

## 色域转换功能(CSC)

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

支持的转换格式如下：

* 支持从YUV420SP、YUYV、YUV422SP、AYUV444转到RGB888、BGR888。
* 支持从XRGB8888、ARGB8888、RGB888转到YVU444SP、YUV444SP、YUV400。

### 静态配置

静态AIPP配置色域转化矩阵示例如下。

```proto
csc_func {
    switch: true
    matrix_r0c0: 256
    matrix_r0c1: 454
    matrix_r0c2: 0
    matrix_r1c0: 256
    matrix_r1c1: -88
    matrix_r1c2: -183
    matrix_r2c0: 256
    matrix_r2c1: 0
    matrix_r2c2: 359
    output_bias_0: 0
    output_bias_1: 0
    output_bias_2: 0
    input_bias_0: 0
    input_bias_1: 128
    input_bias_2: 128
}
```

### 动态配置

指定输出的色域格式，动态场景下，inputFormat可以改变，但是output\_format不可变，否则会报错，因为输出的格式一般是固定的。

```proto
csc_func {
    switch: true
    dynamic: true
    output_format: RGB888_U8
    color_space: JPEG
}
```

## 图片缩放(Resize)

图片缩放功能支持图片放大缩小，采用双线性插值方式进行缩放。缩放输出图片最小为16x16，缩放输出最大为448x448。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```proto
resize_func {
    switch: true
    resize_output_w: 182
    resize_output_h: 182
}
```

### 动态配置

resize\_output\_w、resize\_output\_h为预分配最大size。

```proto
resize_func {
    switch: true
    dynamic: true
    resize_output_w: 250
    resize_output_h: 200
}
```

## 数据类型转换(DTC)

数据类型转化功能是指将输入的图片数据类型通过转化公式转换为FP16类型送给后续模块计算，实际为依次执行减均值、减最小值和乘方差操作。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```proto
dtc_func {
    switch: true
    mean_chn_0: 4
    mean_chn_1: 4
    mean_chn_2: 4
    min_chn_0: 2.0
    min_chn_1: 2.0
    min_chn_2: 2.0
    var_reci_chn_0: 2.0
    var_reci_chn_1: 2.0
    var_reci_chn_2: 2.0
}
```

### 动态配置

可以不写具体的参数，在动态创建input tensor时指定。

```proto
dtc_func {
    switch: true
    dynamic: true
}
```

## 图片旋转(Rotation)

旋转功能支持图片旋转90°、180°和270°，以适配手机在不同方向时的图像数据。当前旋转功能只支持静态单算子场景，动态场景以及卷积融合场景不支持。静态配置如下。

```proto
rotate_para {
    switch: true
    dynamic: true
    rotation_angle: 0.0
}
```

## 图片补边

图片补边功能支持在图片上下左右padding指定大小的数据。 padding的数据可以按通道来设置不同的值，最多补四个通道，如果有的通道没有设置的话，就默认补0，上下左右Padding的大小最大为32，即最多上下各补32行，左右各补32列。

* 当crop或resize作为最后一个AIPP算子时，它的输出shape固定，即输出shape不可动态调整。后面如果接卷积，卷积的输入shape就是crop或resize的输出shape。
* 当crop或者resize后接padding算子时

  + 如果padding算子是静态的，那么padding算子前面的crop或resize也相当于是静态的，输出shape固定不变，crop或resize的输出shape加上padding的值就是后面卷积的shape。
  + 如果padding算子是动态的，那么padding算子的四个padding值就写0。此时，padding算子前的crop或resize的输出就是后面卷积的shape。动态时可以调整参数值，但是要保证最终的输出等于卷积的输入。

dynamic不写或者写成"false"表示静态配置，写成"true"表示动态配置。

### 静态配置

```proto
padding_func {
    switch: true
    left_padding_size: 21
    right_padding_size: 21
    top_padding_size: 21
    bottom_padding_size: 21
    padding_value_chn_0: 20.0
    padding_value_chn_1: 20.0
    padding_value_chn_2: 20.0
    padding_value_chn_3: 20.0
}
```

### 动态配置

padding算子是动态的，padding算子的四个padding值就写0，padding value的值在动态创建input tensor时指定。

```proto
padding_func {
    switch: true
    dynamic: true
    left_padding_size: 0
    right_padding_size: 0
    top_padding_size: 0
    bottom_padding_size: 0
}
```

## 完整AIPP动态配置示例

```proto
aipp_op {
    input_para {
        shape {
            src_image_size_w: 480
            src_image_size_h: 384
        }
    }
    crop_func {
        switch: true
        dynamic: true
        load_start_pos_w: 50
        load_start_pos_h: 50
        crop_size_w: 150
        crop_size_h: 150
    }
    resize_func {
        switch: true
        dynamic: true
        resize_output_w: 250
        resize_output_h: 200
    }
    padding_func {
        switch: true
        dynamic: true
        left_padding_size: 0
        right_padding_size: 0
        top_padding_size: 0
        bottom_padding_size: 0
    }
    swap_func {
        dynamic: true
        ax_swap_switch: true
    }
    csc_func {
        switch: true
        dynamic: true
        output_format: RGB888_U8
        color_space: JPEG
    }
    dtc_func {
        switch: true
        dynamic: true
    }
}
```

## 完整AIPP静态配置

```proto
aipp_op {
    input_para {
        shape {
            src_image_size_w: 480
            src_image_size_h: 384
        }
        format: AYUV444_U8
    }
    crop_func {
        switch: true
        load_start_pos_w: 50
        load_start_pos_h: 50
        crop_size_w: 150
        crop_size_h: 150
    }
    resize_func {
        switch: true
        resize_output_w: 182
        resize_output_h: 182
    }
    padding_func {
        switch: true
        left_padding_size: 21
        right_padding_size: 21
        top_padding_size: 21
        bottom_padding_size: 21
    }
    swap_func {
        ax_swap_switch: true
    }
    csc_func {
        switch: true
        matrix_r0c0: 256
        matrix_r0c1: 454
        matrix_r0c2: 0
        matrix_r1c0: 256
        matrix_r1c1: -88
        matrix_r1c2: -183
        matrix_r2c0: 256
        matrix_r2c1: 0
        matrix_r2c2: 359
        output_bias_0: 0
        output_bias_1: 0
        output_bias_2: 0
        input_bias_0: 0
        input_bias_1: 128
        input_bias_2: 128
    }
    dtc_func {
        switch: true
        mean_chn_0: 4
        mean_chn_1: 4
        mean_chn_2: 4
        min_chn_0: 2.0
        min_chn_1: 2.0
        min_chn_2: 2.0
        var_reci_chn_0: 2.0
        var_reci_chn_1: 2.0
        var_reci_chn_2: 2.0
}
    rotate_func {
        switch: true
        rotate_angle: 180.0
    }
}
```

## 动静态混合配置示例

动静混合场景不支持配置rotate旋转参数，因为此时模型是动态的，动态场景暂不支持rotate旋转参数的配置。

```proto
aipp_op {
    input_para {
        shape {
            src_image_size_w: 200
            src_image_size_h: 200
        }
        format: ARGB8888_U8
    }
    crop_func {
        switch: true
        dynamic: true
        crop_size_w: 100
        crop_size_h: 100
    }
    resize_func {
        switch: true
        resize_output_w: 200
        resize_output_h: 200
    }
    padding_func {
        switch: true
        right_padding_size: 24
        bottom_padding_size: 24
    }
    swap_func {
        rbuv_swap_switch: true
        ax_swap_switch: true
    }
    dtc_func {
        switch: true
        mean_chn_0: 4
        mean_chn_1: 4
        mean_chn_2: 4
        min_chn_0: 2.0
        min_chn_1: 2.0
        min_chn_2: 2.0
        var_reci_chn_0: 2.0
        var_reci_chn_1: 2.0
        var_reci_chn_2: 2.0
    }
}
```
