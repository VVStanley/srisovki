function buildTree(items, boost) {
    items.forEach(item => {
        if (item.id in boost && boost[item.id].length > 0) {
            item["hasChildren"] = true;
            item["children"] = [];
            item["children"] = boost[item.id].filter(val => val);
            // buildTree(boost[item.id], boost);
        } else {
            item["hasChildren"] = false;
        }
    });
    return items;
}

export default {
    install(Vue, options) {
        Vue.prototype.$createTreeForComments = function(data=null) {
            if (!data) data = [];
            let boost = [], parents = [];
            data.forEach(item => {
                console.log(item)
                if (item.parent == null) {
                    boost[item.id] = [];
                    parents.push(item);
                    return;
                }
            })
        },
        Vue.prototype.$createTreePID = function(data=null) {
            /* Строим дерево с помощью parent и id
            Возвращаем массив объектов вида:
            [{ 
                data: data,  
                hasChildren: true,
                children: [
                    {
                        data: data,
                        hasChildren: false,
                    },
                    {...}
                    ]
            },
            {...}
            ]
            */
            if (!data) data = [];
            let boost = [], parents = [];

            data.forEach(item => {
                item.label = item.name
                if (item.parent == null) {
                    boost[item.id] = [];
                    parents.push(item);
                    return;
                }
                if (item.parent in boost) {
                    boost[item.parent][item.id] = item;
                } else {
                    boost[item.parent] = [];
                    boost[item.parent][item.id] = item;
                }
            });
            return buildTree(parents, boost);
        }
    }
}