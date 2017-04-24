angular.module('cafealone.controller')
    .controller('cafeDetailCtrl', function($scope, $http) {
        var cafeId = location.pathname.replace('/cafe/', '');
        console.log(cafeId);

        $http({
            method:'GET',
            url:'/api/cafes/'+cafeId
        }).then(
            function success(response) {
                console.log(response.data);
                $scope.cafe = response.data;
            },
            function error(response) {
                console.log(response.data);
            }
        );
    });