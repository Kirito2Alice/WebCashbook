<template>
    <el-container>
        <el-header>
            <img src="../assets/docker_logo.png">
            <el-button @click="logout" type="info">退出</el-button>
            <div><p>{{name}}</p></div>
            <el-avatar icon="el-icon-user"></el-avatar>
        </el-header>
        <el-container>
            <el-aside width="200px">
                <el-menu router unique-opened active-text-color='#4099CD' background-color='#777' text-color='#ffffff'>
                    <el-submenu :index="item.id + ''" v-for="item in menuinfo" :key="item.id">
                        <template slot="title">
                            <i class="el-icon-location"></i>
                            <span>{{item.authName}}</span>
                        </template>
                        <el-menu-item :index="'/' + subitem.path" v-for="subitem in item.children" :key="subitem.id">
                            <template slot="title">
                                <i class="el-icon-location"></i>
                                <span>{{subitem.authName}}</span>
                            </template>
                        </el-menu-item>
                    </el-submenu>
                </el-menu>
            </el-aside>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
export default {

  data () {
    return {
      name: '',
      menuinfo: [
        {
          id: 100,
          authName: '商品管理',
          path: null,
          children: [
            {
              id: 101,
              authName: '商品列表',
              path: 'goods',
              children: []
            }]
        },
        {
          id: 200,
          authName: '人员管理',
          path: null,
          children: [
            {
              id: 201,
              authName: '人员列表',
              path: 'user',
              children: []
            }]
        }]
    }
  },
  methods: {
    logout () {
      window.sessionStorage.removeItem('token')
      this.$router.push('/')
    }
  },
  mounted () {
    this.name = window.sessionStorage.name
  }
}
</script>

<style>
    .el-container {
        height: 100%;
    }

    .el-header {
        background-color: #888;
    }

    .el-header img {
        margin-left: 45px;
        height: 100%;
    }

    .el-aside {
        background-color: #777;
    }

    .el-button {
        float: right;
        position: relative;
        top: 17.5%;
    }

    .el-avatar {
        float: right;
        position: relative;
        top: 17.5%;
    }

    .el-header div{
        float: right;
        position: relative;
        top: 10.5%;
        margin-left: 10px;
        margin-right: 50px;
    }

    .el-aside .el-menu{
        border: 0;
    }
</style>
