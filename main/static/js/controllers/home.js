angular.module('cafealone.controller')
    .controller('homeCtrl', function($scope, $http) {
        $http({
            method: 'GET',
            url: '/api/cafes/'
        }).then(
            function success(response) {
                console.log(response.data);
                $scope.cafes = response.data;
            },
            function error(response) {
                console.log(response.data);
            }
        )
    });