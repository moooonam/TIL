<template>
  <div>
    <hr>
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @input="fromparent">
    <h3>App : {{ appData }}</h3>
    <h3>Child : {{ childData }}</h3>
    <AppChild :app-data="appData" :parent-data="parentData" @from-child="fromChild"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'
export default {
  components: { AppChild },
    name: "AppParent",
    props: {
        appData: String,
    },
    data: function(){
        return {
            parentData: "",
            childData: "",
        }

    },
    methods: {
        fromparent : function() {
            this.$emit("from-parent", this.parentData)
        },
        fromChild(cd) {
            this.childData = cd
            this.$emit("from-child", this.childData)
        }
    }
}
</script>

<style>

</style>