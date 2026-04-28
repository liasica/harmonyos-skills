---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-example-of-the-operator-json
title: 算子json配置文件样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 调测工具样例与参数说明 > 算子json配置文件样例
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55b372228ea81a7afdbbce947ba062d003c70f6af540d7629eaf99be9870240b
---

## 样例1：NPU/CPU调测算子json配置文件样例

说明

* 在"param\_type"："optional"时， "ignore" : true，表示不需要该输入。
* 在"param\_type"："required"时，"ignore"不能配置为true。

```
1. {
2. "op_type": "FlashAttentionScore",
3. "data_script": "./flash_attention_score_golden.py",
4. "gen_data": true,
5. "inputs": [
6. {
7. "name": "query",
8. "dtype": "float16",
9. "format": "ND",
10. "ignore": false,
11. "shape": [24,144,1280],
12. "param_type": "required",
13. "data_file": "q.bin"
14. },
15. {
16. "name": "key",
17. "dtype": "float16",
18. "format": "ND",
19. "ignore": false,
20. "shape": [24,144,1280],
21. "param_type": "required",
22. "data_file": "k.bin"
23. },
24. {
25. "name": "value",
26. "dtype": "float16",
27. "format": "ND",
28. "ignore": false,
29. "shape": [24,144,1280],
30. "param_type": "required",
31. "data_file": "v.bin"
32. },
33. ],
34. "outputs": [
35. {
36. "name": "softmax_max",
37. "dtype": "float32",
38. "format": "ND",
39. "shape": [24,20,144,8],
40. "ignore": false,
41. "param_type": "required",
42. "data_file": null
43. },
44. {
45. "name": "softmax_sum",
46. "dtype": "float32",
47. "format": "ND",
48. "shape": [24,20,144,8],
49. "ignore": false,
50. "param_type": "required",
51. "data_file": null
52. },
53. {
54. "name": "softmax_out",
55. "dtype": "float16",
56. "format": "ND",
57. "shape": [24,20,144,144],
58. "ignore": false,
59. "param_type": "required",
60. "data_file": null
61. },
62. {
63. "name": "attention_out",
64. "dtype": "float16",
65. "format": "ND",
66. "shape": [24,20,144,64],
67. "ignore": false,
68. "param_type": "required",
69. "data_file": "attention_out.bin"
70. }
71. ],
72. "attrs": [
73. {
74. "name": "scale_value",
75. "dtype": "float",
76. "value": 1.0
77. },
78. {
79. "name": "keep_prob",
80. "dtype": "float",
81. "value": 0.8
82. },
83. {
84. "name": "pre_tokens",
85. "dtype": "int",
86. "value": 2147483647
87. },
88. {
89. "name": "next_tokens",
90. "dtype": "int",
91. "value": 2147483647
92. },
93. {
94. "name": "head_num",
95. "dtype": "int",
96. "value": 20
97. },
98. {
99. "name": "input_layout",
100. "dtype": "string",
101. "value": "BSH"
102. },
103. {
104. "name": "inner_precise",
105. "dtype": "int",
106. "value": 0
107. }
108. ]
109. }
```

## 样例2：tensor list json配置文件样例

```
1. {
2. "op_type": "IncreFlashAttention",
3. "data_script": "",
4. "gen_data": false,
5. "inputs": [
6. {
7. "name": "query",
8. "dtype": "float16",
9. "format": "ND",
10. "ignore": false,
11. "shape": [4, 5, 1, 128],
12. "param_type": "required",
13. "data_file": "/home/data/input/q.bin"
14. },
15. [{
16. "name": "key0",
17. "dtype": "float16",
18. "format": "ND",
19. "ignore": false,
20. "shape": [1,5,8192,128],
21. "param_type": "required",
22. "data_file": "/home/data/input/k_0.bin"
23. },{
24. "name": "key1",
25. "dtype": "float16",
26. "format": "ND",
27. "ignore": false,
28. "shape": [1,5,8192,128],
29. "param_type": "required",
30. "data_file": "/home/data/input/k_1.bin"
31. },{
32. "name": "key2",
33. "dtype": "float16",
34. "format": "ND",
35. "ignore": false,
36. "shape": [1,5,8192,128],
37. "param_type": "required",
38. "data_file": "/home/data/input/k_2.bin"
39. },{
40. "name": "key3",
41. "dtype": "float16",
42. "format": "ND",
43. "ignore": false,
44. "shape": [1,5,8192,128],
45. "param_type": "required",
46. "data_file": "/home/data/input/k_3.bin"
47. }],
48. [{
49. "name": "value0",
50. "dtype": "float16",
51. "format": "ND",
52. "ignore": false,
53. "shape": [1,5,8192,128],
54. "param_type": "required",
55. "data_file": "/home/data/input/v_0.bin"
56. },{
57. "name": "value1",
58. "dtype": "float16",
59. "format": "ND",
60. "ignore": false,
61. "shape": [1,5,8192,128],
62. "param_type": "required",
63. "data_file": "/home/data/input/v_1.bin"
64. },{
65. "name": "value2",
66. "dtype": "float16",
67. "format": "ND",
68. "ignore": false,
69. "shape": [1,5,8192,128],
70. "param_type": "required",
71. "data_file": "/home/data/input/v_2.bin"
72. },{
73. "name": "value3",
74. "dtype": "float16",
75. "format": "ND",
76. "ignore": false,
77. "shape": [1,5,8192,128],
78. "param_type": "required",
79. "data_file": "/home/data/input/v_3.bin"
80. }],
81. {
82. "name": "padding_mask",
83. "dtype": "float16",
84. "format": "ND",
85. "ignore": false,
86. "shape": null,
87. "param_type": "optional",
88. "data_file": null
89. },
90. {
91. "name": "atten_mask",
92. "dtype": "float16",
93. "format": "ND",
94. "ignore": false,
95. "shape": [4,1,8192],
96. "param_type": "optional",
97. "data_file": "/home/data/input/attenMask.bin"
98. },
99. {
100. "name": "actual_seq_lengths",
101. "dtype": "int64",
102. "format": "ND",
103. "ignore": false,
104. "shape": null,
105. "param_type": "optional",
106. "data_file": ""
107. },
108. {
109. "name": "deq_scale1",
110. "dtype": "uint64",
111. "format": "ND",
112. "ignore": false,
113. "shape": null,
114. "param_type": "optional",
115. "data_file": null
116. },
117. {
118. "name": "quant_scale1",
119. "dtype": "float32",
120. "format": "ND",
121. "ignore": false,
122. "shape": null,
123. "param_type": "optional",
124. "data_file": null
125. },
126. {
127. "name": "deq_scale2",
128. "dtype": "uint64",
129. "format": "ND",
130. "ignore": false,
131. "shape": null,
132. "param_type": "optional",
133. "data_file": null
134. },
135. {
136. "name": "quant_scale2",
137. "dtype": "float32",
138. "format": "ND",
139. "ignore": false,
140. "shape": null,
141. "param_type": "optional",
142. "data_file": null
143. },
144. {
145. "name": "quant_offset2",
146. "dtype": "float32",
147. "format": "ND",
148. "ignore": false,
149. "shape": null,
150. "param_type": "optional",
151. "data_file": null
152. }
153. ],
154. "outputs": [
155. {
156. "name": "attention_out",
157. "dtype": "float16",
158. "format": "ND",
159. "shape": [4, 5, 1, 128],
160. "ignore": false,
161. "param_type": "required",
162. "data_file": "/home/data/output/y_add.bin"
163. }
164. ],
165. "attrs": [
166. {
167. "name": "num_heads",
168. "dtype": "int",
169. "value": 5
170. },
171. {
172. "name": "scale_value",
173. "dtype": "float",
174. "value": 2.0
175. },
176. {
177. "name": "input_layout",
178. "dtype": "string",
179. "value": "BNSD"
180. },
181. {
182. "name": "num_key_value_heads",
183. "dtype": "int",
184. "value": 5
185. }
186. ]}
```

## 样例3：tiling调测json配置文件样例

```
1. {
2. "op_type": "FlashAttentionScore",
3. "data_script": "./flash_attention_score_golden.py",
4. "gen_data": true,
5. "inputs": [
6. {
7. "name": "query",
8. "dtype": "float16",
9. "format": "ND",
10. "ignore": false,
11. "shape": [24,144,1280],
12. "param_type": "required",
13. "data_file": "q.bin"
14. },
15. {
16. "name": "key",
17. "dtype": "float16",
18. "format": "ND",
19. "ignore": false,
20. "shape": [24,144,1280],
21. "param_type": "required",
22. "data_file": "k.bin"
23. },
24. {
25. "name": "value",
26. "dtype": "float16",
27. "format": "ND",
28. "ignore": false,
29. "shape": [24,144,1280],
30. "param_type": "required",
31. "data_file": "v.bin"
32. },
33. {
34. "name": "real_shift",
35. "dtype": "float16",
36. "format": "ND",
37. "ignore": false,
38. "shape": null,
39. "param_type": "optional",
40. "data_file": null
41. },
42. {
43. "name": "drop_mask",
44. "dtype": "uint8",
45. "format": "ND",
46. "ignore": false,
47. "shape": [1244160],
48. "param_type": "optional",
49. "data_file": "drop_mask.bin"
50. },
51. {
52. "name": "padding_mask",
53. "dtype": "float16",
54. "format": "ND",
55. "ignore": false,
56. "shape": null,
57. "param_type": "optional",
58. "data_file": null
59. },
60. {
61. "name": "atten_mask",
62. "dtype": "bool",
63. "format": "ND",
64. "ignore": false,
65. "shape": null,
66. "param_type": "optional",
67. "data_file": null
68. },
69. {
70. "name": "prefix",
71. "dtype": "int64",
72. "format": "ND",
73. "ignore": false,
74. "shape": null,
75. "param_type": "optional",
76. "data_file": null
77. }
78. ],
79. "outputs": [
80. {
81. "name": "softmax_max",
82. "dtype": "float32",
83. "format": "ND",
84. "shape": [24,20,144,8],
85. "ignore": false,
86. "param_type": "required",
87. "data_file": null
88. },
89. {
90. "name": "softmax_sum",
91. "dtype": "float32",
92. "format": "ND",
93. "shape": [24,20,144,8],
94. "ignore": false,
95. "param_type": "required",
96. "data_file": null
97. },
98. {
99. "name": "softmax_out",
100. "dtype": "float16",
101. "format": "ND",
102. "shape": [24,20,144,144],
103. "ignore": false,
104. "param_type": "required",
105. "data_file": null
106. },
107. {
108. "name": "attention_out",
109. "dtype": "float16",
110. "format": "ND",
111. "shape": [24,20,144,64],
112. "ignore": false,
113. "param_type": "required",
114. "data_file": "attention_out.bin"
115. }
116. ],
117. "attrs": [
118. {
119. "name": "scale_value",
120. "dtype": "float",
121. "value": 1.0
122. },
123. {
124. "name": "keep_prob",
125. "dtype": "float",
126. "value": 0.8
127. },
128. {
129. "name": "pre_tokens",
130. "dtype": "int",
131. "value": 2147483647
132. },
133. {
134. "name": "next_tokens",
135. "dtype": "int",
136. "value": 2147483647
137. },
138. {
139. "name": "head_num",
140. "dtype": "int",
141. "value": 20
142. },
143. {
144. "name": "input_layout",
145. "dtype": "string",
146. "value": "BSH"
147. },
148. {
149. "name": "inner_precise",
150. "dtype": "int",
151. "value": 0
152. }
153. ]
154. }
```

## 样例4：kernel直调json配置样例

```
1. {
2. "op_type": "add_custom",
3. "data_script": "",
4. "gen_data": false,
5. "params": [
6. {
7. "name": "x",
8. "dtype": "float16",
9. "param_type": "input",
10. "shape": [
11. 1,16384
12. ],
13. "data_file": "input_x.bin"
14. },
15. {
16. "name": "y",
17. "dtype": "float16",
18. "param_type": "input",
19. "shape": [
20. 1,16384
21. ],
22. "data_file": "input_y.bin"
23. },
24. {
25. "name": "z",
26. "dtype": "float16",
27. "param_type": "output",
28. "shape": [
29. 1,16384
30. ],
31. "data_file": "golden.bin"
32. },
33. {
34. "name": "tileNumIn",
35. "dtype": "uint32",
36. "param_type": "input",
37. "shape": null,
38. "data_value": 8
39. }
40. ],
41. "kernel_info": {
42. "kernel_source": ["add_custom.cpp"],
43. "kernel_name": "add_custom",
44. "kernel_includes": []
45. }

47. }
```
