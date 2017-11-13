var memoApp = angular.module('memoApp', ['ngRoute']);

var urlHeader = "http:localhost:8000";
memoApp.config(['$routeProvider',
  function config($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: '/static/templates/index.html',
        controller: 'mainController'
      }).
      when('/memos', {
        templateUrl: '/static/templates/memo.html',
        controller: 'MemoController'
      }).
/*      when('/polls/:question_id', {
        templateUrl: '/static/templates/detail.html',
        controller: 'QuestionController'
      }).
*/
      otherwise('/');
  }
]);

memoApp.controller('mainController',
  function mainController($scope) {
    $scope.sampleText = "Welcome. This is the first screen";
});

memoApp.controller('MemoController',
  function MemoController($scope, $http) {
    $scope.memos = null;
    $http({
      method: 'GET',
      url: '/memos/',
    }).then(function (response) {
      $scope.memos = response.data;
    });
});