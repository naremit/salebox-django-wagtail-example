const { dest, parallel, series, src, watch } = require('gulp');
const concat = require('gulp-concat');
const minifycss = require('gulp-minify-css');
const sass = require('gulp-sass');
const uglify = require('gulp-uglify');

function css(cb) {
    return src([
        'sass/salebox.scss',
    ])
    .pipe(sass())
    .pipe(minifycss())
    .pipe(concat('salebox.css'))
    .pipe(dest('www/static/css/'));
}

function js(cb) {
    return src([
        'node_modules/jquery/dist/jquery.min.js',
        'node_modules/popper.js/dist/umd/popper.min.js',
        'node_modules/bootstrap/dist/js/bootstrap.min.js',
        'www/staticsrc/js/*.js',
    ])
    .pipe(concat('salebox.js'))
    .pipe(uglify())
    .pipe(dest('www/static/'));
}