// demo data
var data = {
  name: 1,
  children: [
    { name: 1 },
    { name: 5, children: [
        {name: 3},
		{name: 13,children: [
            { name: 17 },
            { name: 69 }
            ]}]},
    { name: 21},
    { name: 85}
  ]
}

// define the item component
Vue.component('item', {
  template: '#item-template',
  props: {
    model: Object
  },
  data: function () {
    return {
      open: true
    }
  },
  computed: {
    isFolder: function () {
      return this.model.children &&
        this.model.children.length
    }
  },
  methods: {
    toggle: function () {
      if (this.isFolder) {
        this.open = !this.open
      }
    },
    changeType: function () {
      if (!this.isFolder) {
        Vue.set(this.model, 'children', [])
        this.addChild()
        this.open = true
      }
    },
    addChild: function () {
		console.log(this.model.name);
		if(+this.model.name %3!=0){
		  this.model.children.push(
			{name: v(+this.model.name)},
			{name: h(v(+this.model.name))},
			{name: h(h(v(+this.model.name)))},
			{name: h(h(h(v(+this.model.name))))}
		  )
		}
    }
  }
})

// boot up the demo
var demo = new Vue({
  el: '#demo',
  data: {
    treeData: data
  }
})
