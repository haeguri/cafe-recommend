angular.module('cafealone', [
    'cafealone.controller',
    'ngRoute'
    // 'cafealone.factory'
]).config(function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', {
            templateUrl:'/static/partials/home.html',
            controller:'homeCtrl'
        })
        .when('/cafe/add', {
            templateUrl:'/static/partials/cafe_add.html',
            controller:'cafeAddCtrl'
        })
        .when('/cafe/:cafeId', {
            templateUrl:'/static/partials/cafe_detail.html',
            controller:'cafeDetailCtrl'
        })
        .otherwise({redirectTo: '/'});

    $locationProvider.html5Mode(true);

    // example.com#home
    // example.com#index
}).controller('rootCtrl', function($scope) {
    console.log('rootctrl');
});