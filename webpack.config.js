const path = require('path');
const webpack = require("webpack");
const CopyPlugin = require('copy-webpack-plugin');
const { VueLoaderPlugin } = require("vue-loader");
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');


module.exports = {
    entry: {
        // Общее
        common: './src/entries/common.js',

        // Фронт
        post: './src/entries/post.js',
        category_step_drawing: './src/entries/categoryStepDrawing.js',

        // Компоненты
        post_components: './src/entries/postComponents.js',
        category_components: './src/entries/categoryComponents.js',
        what_colorize: './src/entries/what_colorize.js',
        image_cropper: './src/entries/imageCropper.js'
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, './static_src/js')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: [
                    path.resolve(__dirname, './node_modules/'),
                    path.resolve(__dirname, './src/plugins/')
                ]
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
            },
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: { sourceMap: true }
                    },
                    {
                        loader: 'sass-loader',
                        options: { sourceMap: true }
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: { sourceMap: true }
                    },
                    {
                        loader: 'postcss-loader',
                        options: { config: { path: 'postcss.config.js' } }
                    },
                ],
                exclude: '/node_modules/',
            },
            {
                test: /\.(woff|woff2|eot|ttf|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '../font/[name].[ext]'
                }
            },
            {
                test: /\.(jpg|png|gif)$/,
                loader: 'file-loader',
                options: {
                    name: '../img_src/[name].[ext]'
                }
            }
        ]
    },
    // watch: true,
    watchOptions: {
        ignored: [
            path.resolve(__dirname, './node_modules/'),
            path.resolve(__dirname, './src/app_plugins/')
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.js'
        }
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery',
            'window.$': 'jquery',
            Promise: 'es6-promise',
        }),
        new MiniCssExtractPlugin({
            filename: '../css/[name].css'
        }),
        new VueLoaderPlugin(),
        new CleanWebpackPlugin(),
        new CopyPlugin([
            {from: `./src/img`, to: `../img`},
            {from: `./src/files`, to: `../`},
            // {from: `./src/favicon.ico`, to: `../[name].[ext]`},
            // {from: `./src/favicon.png`, to: `../[name].[ext]`},
            // {from: `./src/robots.txt`, to: `../[name].[ext]`},
            // {from: `./src/ads.txt`, to: `../[name].[ext]`},
        ]),
    ]
}