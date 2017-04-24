angular.module('cafealone.controller')
    .controller('cafeAddCtrl', function($scope, $http) {
        console.log('cafe add controller');
        $scope.addCafe = function() {
            // console.log($scope.name, $scope.desc);
            $http({
                method: 'get',
                url: '/api/cafes',
                params: {
                    flag: $scope.flag
                }
            }).then(
                function success(response) {
                    console.log('cafe add success', response);
                },
                function error(response) {
                    console.log('cafe add error', response);
                }
            )
        };
    });