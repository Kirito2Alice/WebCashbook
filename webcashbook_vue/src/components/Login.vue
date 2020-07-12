<template>
    <div class="login_container">
        <div class="login_box">
            <!-- 头像图片区域 -->
            <div class="avatar_box">
                <img src="../assets/logo.png">
            </div>
            <!-- 登录表单区域 -->
            <el-form label-width="0px">
                <el-form-item>
                    <el-input prefix-icon="el-icon-s-custom" placeholder="请输入用户名"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-input prefix-icon="el-icon-lock" placeholder="请输入密码"></el-input>
                </el-form-item>

                <el-row>
                    <el-col class="cols_btn" :span="12">
                        <el-button type="primary">登录</el-button>
                    </el-col>

                    <el-col class="cols_btn" :span="12">
                        <el-button type="info">重置</el-button>
                    </el-col>
                </el-row>

                <!-- <el-row>
                    <el-button type="primary">登录</el-button>
                    <el-button type="info">重置</el-button>
                </el-row> -->
            </el-form>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.login_container {
    background-color: #2b4b6b;
    height: 100%;
}
.login_container .login_box {
    width: 450px;
    height: 300px;
    background-color:rgba(255,255,255,0.5);
    border-radius: 10px;
    position: absolute;
    left: 50%;
    top: 50%;
    margin-left: -225px;
    margin-top: -150px;
    box-shadow: rgba(255,255,255,0.8);
}
.login_container .login_box .avatar_box {
    width: 130px;
    height: 130px;
    background-color: #fff;
    border: 1px #eee;
    padding: 10px;
    border-radius: 50%;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
}
img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #eee;
}
.cols_btn {
    text-align: center;
}
</style>
