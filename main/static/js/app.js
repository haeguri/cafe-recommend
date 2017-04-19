angular.module('cafealone', [
    'cafealone.controller'
    // 'cafealone.factory'
]).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});