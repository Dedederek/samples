中文|[English](README_EN.md)

**该案例仅仅用于学习，打通流程，不对效果负责，不支持商用。**

#  检测网络应用（C++）<a name="ZH-CN_TOPIC_0219122211"></a>
本应用支持运行在Atlas 200 DK上，实现了对yolov3目标检测网络的推理功能。 

## 软件准备<a name="zh-cn_topic_0219108795_section181111827718"></a>

运行此Sample前，需要按照此章节获取源码包。

1.  <a name="zh-cn_topic_0228757084_section8534138124114"></a>获取源码包。

    **cd $HOME/AscendProjects**  

    **wget https://gitee.com/atlasdevelop/c7x_samples/tree/master/200dk_sample/objectdetection_dynamic_aipp**
            
    
2.  <a name="zh-cn_topic_0219108795_li2074865610364"></a>获取此应用中所需要的原始网络模型。    
 
     -  下载原始网络模型及权重文件至ubuntu服务器任意目录，如:$HOME/yolov3。

        **mkdir -p $HOME/yolov3**

        **wget -P $HOME/yolov3 https://c7xcode.obs.cn-north-4.myhuaweicloud.com/models/yolov3/yolov3.caffemodel** 
 
        **wget -P $HOME/yolov3 https://c7xcode.obs.cn-north-4.myhuaweicloud.com/models/yolov3/yolov3.prototxt**
           
        >![](public_sys-resources/icon-note.gif) **说明：**   
        >- yolov3原始模型网络： https://github.com/maxuehao/YOLOV3/blob/master/yolov3_res18.prototxt 
        >- yolov3原始网络LICENSE地址： https://github.com/maxuehao/caffe/blob/master/LICENSE
        >- C7x对prototxt文件有修改要求，按照[yolov3网络模型prototxt修改](https://support.huaweicloud.com/usermanual-mindstudioc73/atlasmindstudio_02_0112.html)文档对prototxt文件进行修改。这里已经修改完成，直接执行以上命令下载即可。

3.  将原始网络模型转换为适配昇腾AI处理器的模型。  

    1.  设置环境变量
        
        命令行中输入以下命令设置环境变量。

        **cd \$HOME/yolov3**
        
        **export install_path=\$HOME/Ascend/ascend-toolkit/20.0.RC1/x86_64-linux_gcc7.3.0**  

        **export PATH=/usr/local/python3.7.5/bin:\\${install_path}/atc/ccec_compiler/bin:\\${install_path}/atc/bin:\\$PATH**  

        **export PYTHONPATH=\\${install_path}/atc/python/site-packages/te:\\${install_path}/atc/python/site-packages/topi:\\$PYTHONPATH**  

        **export LD_LIBRARY_PATH=\\${install_path}/atc/lib64:\\$LD_LIBRARY_PATH**  

        **export ASCEND_OPP_PATH=\\${install_path}/opp**  

    2.  执行以下命令转换模型。

        **atc --model=\\$HOME/yolov3/yolov3.prototxt --weight=\\$HOME/yolov3/yolov3.caffemodel --framework=0 --output=\\$HOME/yolov3/yolov3 --soc_version=Ascend310 --insert_op_conf=\\$HOME/AscendProjects/objectdetection_dynamic_aipp/aipp_objectdetection.cfg**

    
5.  将转换好的模型文件（.om文件）添加到项目工程中：

    cp /home/ascend/yolov3/yolov3.om /home/ascend/AscendProjects/objectdetection_dynamic_aipp/model/

## 环境配置   

**注：服务器上已安装OpenCV、交叉编译工具可跳过此步骤。**  
    
- 安装编译工具  
  **sudo apt-get install -y g++\-aarch64-linux-gnu g++\-5-aarch64-linux-gnu** 

- 安装OpenCV 
      
    请参考 **https://gitee.com/ascend/samples/tree/master/common/install_opencv/for_atlas200dk**    

## 编译<a name="zh-cn_topic_0219108795_section3723145213347"></a>
1.  打开对应的工程。

    以Mind Studio安装用户在命令行进入安装包解压后的“MindStudio-ubuntu/bin”目录，如：$HOME/MindStudio-ubuntu/bin。执行如下命令启动Mind Studio。

    **./MindStudio.sh**

    启动成功后，打开**objectdetection_dynamic_aipp**工程，如图 1所示。   

    ![打开工程](https://images.gitee.com/uploads/images/2020/0924/161134_1d437fbf_7985487.png "屏幕截图.png"))

    **图 1**  打开objectdetection工程<a name="zh-cn_topic_0228461902_zh-cn_topic_0203223265_fig11106241192810"></a>  

2.  开始编译，打开Mind Studio工具，在工具栏中点击**Build \> Edit Build Configuration**。  
    选择Target OS 为Centos7.6，如[图2 配置编译]所示。

    ![配置编译](https://images.gitee.com/uploads/images/2020/0923/104800_bd70575c_8083019.png "build成功.png")

    **图 2**  配置编译<a name="zh-cn_topic_0203223265_fig17414647130"></a>  
    
    之后点击**Build \> Build \> Build Configuration**，如图3 成功编译，会在目录下生成build和out文件夹。

    ![成功编译](https://images.gitee.com/uploads/images/2020/0924/162201_eef5f2df_7985487.png "屏幕截图.png")
    **图 3**  编译操作及生成文件<a name="zh-cn_topic_0203223265_fig1741464713019"></a>  

    >![](public_sys-resources/icon-notice.gif) **须知：**   
    >首次编译工程时，**Build \> Build**为灰色不可点击状态。需要点击**Build \> Edit Build Configuration**，配置编译参数后再进行编译。  
## 运行<a name="zh-cn_topic_0219108795_section1620073406"></a>
1.  在Mind Studio工具的工具栏中找到Run按钮，单击  **Run \> Edit Configurations**。  
    在Command Arguments 中添加运行参数 **../data**（输入图片的路径），之后分别点击Apply、OK。如图 配置运行 所示。
   
    ![配置运行](https://images.gitee.com/uploads/images/2020/0924/163014_4fc1f847_7985487.png "屏幕截图.png")
    **图 4**  配置运行  
 
2.  单击  **Run \> Run 'objectdetection'**，如图 程序已执行示意图 所示，可执行程序已经在开发者板执行。  

   ![程序已执行](https://images.gitee.com/uploads/images/2020/0924/163237_4c892d8e_7985487.png "屏幕截图.png")
    **图 5**  程序已执行示意图<a name="zh-cn_topic_0203223265_fig93931954162719"></a>  

3.  查看运行结果。

    推理结果图片保存在工程下的“output \> outputs”目录下以时间戳命名的文件夹内。  

    ![结果](https://images.gitee.com/uploads/images/2020/0923/105425_9df9344a_8083019.png "result.png")