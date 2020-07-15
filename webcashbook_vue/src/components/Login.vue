<template>
    <div class="login_container">
        <div class="login_box">
            <!-- 头像图片区域 -->
            <div class="avatar_box">
                <img src="../assets/github_logo.png">
            </div>
            <!-- 登录表单区域 -->
            <el-form ref="loginFormRef" :model='loginForm' :rules="loginFormRules" class="form_login" label-width="0px">
                <el-form-item prop="accoutname">
                    <el-input v-model="loginForm.accoutname" prefix-icon="el-icon-s-custom" placeholder="请输入用户名"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input v-model="loginForm.password" prefix-icon="el-icon-lock" placeholder="请输入密码" type='password'></el-input>
                </el-form-item>

                <el-row>
                    <el-col class="cols_btn" :span="12">
                        <el-button type="primary" @click="login">登录</el-button>
                    </el-col>

                    <el-col class="cols_btn" :span="12">
                        <el-button type="info" @click="resetLoginForm">重置</el-button>
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
export default {
  data () {
    return {
      loginForm: {
        accoutname: 'kirito',
        password: 'kirito628'
      },
      loginFormRules: {
        accoutname: [
          { required: true, message: '请输入账户名称', trigger: 'blur' },
          { min: 6, max: 12, message: '长度在 6 到 12 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入账户密码', trigger: 'blur' },
          { min: 8, max: 16, message: '长度在 8 到 16 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      this.$refs.loginFormRef.validate(async (valid) => {
        console.log(valid)
        if (!valid) return
        var res = await this.$http.post('login', this.loginForm)
        console.log(res)
        console.log(res.data)
      })
    }
  }
}
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

.form_login {
    width: 80%;
    margin-top: 20%;
    margin-left: 10%;
}

.cols_btn {
    text-align: center;
}
</style>
