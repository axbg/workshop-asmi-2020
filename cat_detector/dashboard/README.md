# dashboard

A web interface built with [Vue.js](https://vuejs.org/) and served originally from a [Amazon S3]() bucket that calls `collector's` endpoints and displays the data in a chart

# 
## Dependencies
- [Vue.js](https://www.npmjs.com/package/vue)
- [vue-material](https://www.npmjs.com/package/vue-material)
- [vue-chartjs](https://www.npmjs.com/package/vue-chartjs)
- [vue2-datepicker](https://www.npmjs.com/package/vue2-datepicker)
- [vue-carousel](https://www.npmjs.com/package/vue-carousel)
#
## Deployment
1. Install [Node.js](https://nodejs.org/en/download/)

2. Install the dependencies
    - `npm install`

3. Update the `Vue.prototype.$baseUrl` variable with `collector's` address in [main.js](./dashboard/src/main.js)

4. - Run the app
        - `npm run serve`

    - Or build it and [serve](https://www.npmjs.com/package/serve) it
        - `npm run build`
        - `serve dist`