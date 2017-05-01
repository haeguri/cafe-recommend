angular.module('cafealone.controller')
    .controller('navbarCtrl', function($scope, $http, $route) {
        $scope.forceReload = function() {
            console.log('reload!');
            $route.reload();
        };
        console.log('navbar controller');
    });