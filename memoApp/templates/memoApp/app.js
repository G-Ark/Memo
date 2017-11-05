var resumeApp = angular.module('resumeApp', ['ui.router']);
resumeApp.config(function($stateProvider, $urlRouterProvider) {
    var location = 'http://localhost:5000/'; 
    $urlRouterProvider.otherwise('/home');    
    $stateProvider
        .state('home', {
            url: '/home',
            templateUrl: location + 'components/home/templates/home.html',
            controller: 'resumeController'
        })
        .state('about', {
            url: '/about',
            templateUrl: location + 'components/about/templates/about.html',
            controller: 'aboutController'
        })
        .state('hire', {
            url: '/hire',
            templateUrl: location + 'components/hire/templates/hire.html'
        })
        .state('contact', {
            url: '/contact',
            templateUrl: location + 'components/contact/templates/contact.html'
        })
        .state('work', {
            url: '/work',
            templateUrl: location + 'components/work/templates/work.html',
            controller: 'workController'
        });
});