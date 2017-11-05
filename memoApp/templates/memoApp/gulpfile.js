var gulp   = require('gulp');
var concat = require('gulp-concat');
var jsonServer = require("gulp-json-srv");
var sass = require('gulp-sass');

//file paths and variable declarations
var sassFiles = '**/*.scss';
var cssDest = 'dest/';
var jsFiles = 'components/**/*.js';
var appJsFile = 'app.js';
var jsDest = 'dest/';
var server = jsonServer.create();

// Start here
gulp.task('build',['styles','scripts','server'], function() {
    
});

//Concat js files
gulp.task('scripts', function(){
    return gulp.src([appJsFile, jsFiles])
            .pipe(concat('scripts.js'))
            .pipe(gulp.dest(jsDest));
});

// compile sass to css
gulp.task('styles', function(){
    gulp.src(sassFiles)
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('styles.css'))
        .pipe(gulp.dest(cssDest));
});

// watch for changes in sass files
gulp.task('watch',function() {
    gulp.watch(sassFiles,['build']);
});

// Run json server. Mostly only for dev
gulp.task('server', function(){
	return gulp.src("../db.json")
        .pipe(server.pipe());
});