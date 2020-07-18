<template>
    <el-container>
        <el-header>
            <img src="../assets/docker_logo.png">
            <el-button type="info">退出</el-button>
        </el-header>
        <el-container>
            <el-aside width="200px">Aside</el-aside>
            <el-main>Main</el-main>
        </el-container>
    </el-container>
</template>

<script>
export default {

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
        top: 15%;
    }
</style>
