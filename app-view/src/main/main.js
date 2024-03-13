import React, { Component } from 'react';
import { Switch, Route, BrowserRouter} from 'react-router-dom'

class Main extends Component {
  render() {
    return (
    <BrowserRouter>
        <Switch>
          <Route exact path="/">
            <Field />
          </Route>
        </Switch>
    </BrowserRouter>
    );
  }
}

export default Main;