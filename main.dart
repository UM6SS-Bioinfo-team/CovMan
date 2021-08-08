//@dart=2.9
import 'package:flutter/material.dart';
import 'package:frontend/constants.dart';
import 'package:frontend/router.dart';

void main() {
  runApp(CovMa());
}

class CovMa extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CovMA',
      initialRoute: Home,
      onGenerateRoute: RouteGenerator.generateRoute,
    );
  }
}
