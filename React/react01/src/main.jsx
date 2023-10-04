import React from 'react';
import ReactDOM from 'react-dom/client';

import {App} from './components/App';

ReactDOM.createRoot(document.querySelector("#root")).render(
    <div>
        <App /> {/* Pode ser chamado das duas formas, mas essa é a mais comum */}
        {/* <App></App>  */}
    </div>
)